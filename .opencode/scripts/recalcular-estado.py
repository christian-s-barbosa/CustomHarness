#!/usr/bin/env python3
"""Recalcula o estado-atual.md (e opcionalmente as notas de conceito) a partir
das observações/avaliações (event-sourcing).

Uso:
  python recalcular-estado.py <vault>              # só estado-atual.md
  python recalcular-estado.py <vault> --conceitos  # também conceitos/<nome>.md
"""
import sys
import os
import re
import glob
import datetime
import frontmatter

BLOOM = ["Lembrar", "Entender", "Aplicar", "Analisar", "Avaliar", "Criar"]
# Um pré-requisito abaixo deste nível (ou não praticado) vira lacuna.
LIMIAR_LACUNA = "Aplicar"


def data_str(d):
    if d is None:
        return ""
    if isinstance(d, (datetime.date, datetime.datetime)):
        return d.isoformat()
    return str(d)


def rank(nivel):
    return BLOOM.index(nivel) if nivel in BLOOM else -1


def intervalo(nivel):
    if nivel in ("Lembrar", "Entender"):
        return 3
    if nivel in ("Aplicar", "Analisar"):
        return 7
    if nivel in ("Avaliar", "Criar"):
        return 21
    return 7


def carregar(vault, tipo):
    """Lê todos os eventos do tipo (avaliacao/observacao), em qualquer projeto."""
    out = []
    padrao = os.path.join(vault, "historico", "**", tipo, "**", "*.md")
    for f in sorted(glob.glob(padrao, recursive=True)):
        try:
            with open(f, encoding="utf-8-sig") as fh:
                fm = frontmatter.loads(fh.read())
            out.append(fm.metadata)
        except Exception:
            pass
    return out


def preservar_secao(caminho, titulo):
    if not os.path.exists(caminho):
        return None
    linhas = open(caminho, encoding="utf-8").read().splitlines()
    res, dentro = [], False
    for l in linhas:
        if l.startswith("## "):
            dentro = (l == "## " + titulo)
            continue
        if dentro:
            res.append(l)
    return res


def preservar_categoria(caminho):
    if not os.path.exists(caminho):
        return ""
    try:
        with open(caminho, encoding="utf-8-sig") as fh:
            fm = frontmatter.loads(fh.read())
        return fm.metadata.get("categoria") or ""
    except Exception:
        return ""


def ler_prereqs(vault):
    """Lê os pré-requisitos (links [[...]]) das notas de conceito existentes."""
    prereqs = {}
    pasta = os.path.join(vault, "conceitos")
    if not os.path.isdir(pasta):
        return prereqs
    for f in glob.glob(os.path.join(pasta, "*.md")):
        nome = os.path.splitext(os.path.basename(f))[0]
        if nome.startswith("_"):
            continue
        secao = preservar_secao(f, "Pré-requisitos")
        if secao:
            for linha in secao:
                for m in re.findall(r"\[\[([^\]|#]+)", linha):
                    prereqs.setdefault(nome, []).append(m.strip())
    return prereqs


def calcular_lacunas(conceitos, prereqs):
    """Lacuna = pré-requisito abaixo do limiar (ou não praticado)."""
    out = []
    for nome in sorted(prereqs):
        for p in prereqs[nome]:
            nivel = conceitos.get(p, {}).get("nivel")
            if nivel is None or rank(nivel) < rank(LIMIAR_LACUNA):
                out.append(f"- [[{nome}]] exige [[{p}]] (nível atual: {nivel or 'não praticado'})")
    return out


def escrever_conceito(vault, nome, info, evid):
    os.makedirs(os.path.join(vault, "conceitos"), exist_ok=True)
    caminho = os.path.join(vault, "conceitos", nome + ".md")
    categoria = preservar_categoria(caminho)
    definicao = preservar_secao(caminho, "Definição")
    sinonimos = preservar_secao(caminho, "Sinônimos")
    prereqs = preservar_secao(caminho, "Pré-requisitos")

    L = []
    L.append("---")
    L.append("tipo: conceito")
    L.append("conceito: " + nome)
    L.append("categoria: " + (categoria or ""))
    L.append("atualizado: " + datetime.date.today().isoformat())
    L.append("---")
    L.append("")
    L.append("# " + nome)
    L.append("")
    L.append("## Definição")
    L.extend(definicao if definicao is not None else ["<o que é>"])
    L.append("")
    L.append("## Sinônimos")
    L.extend(sinonimos if sinonimos is not None else ["- "])
    L.append("")
    L.append("## Pré-requisitos")
    L.extend(prereqs if prereqs is not None else ["- "])
    L.append("")
    L.append("## Nível atual")
    L.append(info["nivel"])
    L.append("")
    L.append("## Evidências")
    if evid:
        for data, txt in evid:
            L.append("- " + data + " — " + txt)
    else:
        L.append("- ...")
    L.append("")

    with open(caminho, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")


def main(vault, com_conceitos):
    vault = os.path.abspath(vault)
    avaliacoes = carregar(vault, "avaliacao")
    observacoes = carregar(vault, "observacoes")

    conceitos = {}
    evidencias = {}
    dreyfus, dreyfus_data = "", ""
    for m in avaliacoes:
        data = data_str(m.get("data"))
        d = m.get("dreyfus") or ""
        if data >= dreyfus_data:
            dreyfus, dreyfus_data = d, data
        for c in (m.get("conceitos") or []):
            nome, nivel = c.get("nome", ""), c.get("nivel", "")
            if not nome or rank(nivel) < 0:
                continue
            evidencias.setdefault(nome, []).append((data, c.get("evidencia", "")))
            cur = conceitos.get(nome)
            if (cur is None or rank(nivel) > rank(cur["nivel"])
                    or (rank(nivel) == rank(cur["nivel"]) and data >= cur["data"])):
                conceitos[nome] = {
                    "nivel": nivel,
                    "evidencia": c.get("evidencia", ""),
                    "data": data,
                    "confianca": c.get("confianca", ""),
                }

    erros = {}
    for m in observacoes:
        data = data_str(m.get("data"))
        for nome in (m.get("erros") or []):
            e = erros.setdefault(nome, {"count": 0, "last": ""})
            e["count"] += 1
            if data > e["last"]:
                e["last"] = data
            evidencias.setdefault(nome, []).append((data, "errou"))

    hoje = datetime.date.today()
    L = []
    L.append("---")
    L.append("tipo: estado-atual")
    L.append("escopo: aluno")
    L.append("atualizado: " + hoje.isoformat())
    L.append("---")
    L.append("")
    L.append("# Estado atual")
    L.append("")
    L.append("> GERADO por `recalcular-estado.py` a partir das observações/avaliações.")
    L.append("> Seções derivadas são recalculadas — não edite. Edite só Metas.")
    L.append("")

    L.append("## Estágio global (Dreyfus)")
    L.append("- " + (dreyfus or "—"))
    L.append("")

    L.append("## Matriz de habilidades (Bloom)")
    L.append("| Conceito | Nível | Evidência | Última prática |")
    L.append("|----------|-------|-----------|----------------|")
    for nome in sorted(conceitos):
        c = conceitos[nome]
        L.append(f"| {nome} | {c['nivel']} | {c['evidencia']} | {c['data']} |")
    L.append("")

    L.append("## Confiança × competência")
    L.append("| Conceito | Confiança | Competência |")
    L.append("|----------|-----------|-------------|")
    for nome in sorted(conceitos):
        c = conceitos[nome]
        L.append(f"| {nome} | {c['confianca'] or '—'} | {c['nivel']} |")
    L.append("")

    L.append("## Erros recorrentes")
    L.append("| Conceito | Ocorrências | Última vez |")
    L.append("|----------|-------------|------------|")
    for nome in sorted(erros):
        e = erros[nome]
        L.append(f"| {nome} | {e['count']} | {e['last']} |")
    L.append("")

    L.append("## Revisão espaçada")
    L.append("| Conceito | Última | Próxima |")
    L.append("|----------|--------|---------|")
    for nome in sorted(conceitos):
        c = conceitos[nome]
        if c["data"]:
            try:
                d = datetime.date.fromisoformat(c["data"])
                prox = d + datetime.timedelta(days=intervalo(c["nivel"]))
                status = "revisar agora" if prox <= hoje else prox.isoformat()
                L.append(f"| {nome} | {c['data']} | {status} |")
            except ValueError:
                pass
    L.append("")

    ea = os.path.join(vault, "estado-atual.md")
    L.append("## Lacunas de pré-requisitos")
    lacunas = calcular_lacunas(conceitos, ler_prereqs(vault))
    L.extend(lacunas if lacunas else ["- ..."])
    L.append("")

    L.append("## Metas")
    metas = preservar_secao(ea, "Metas")
    L.extend(metas if metas is not None else [
        "| Meta | Horizonte | Progresso | Status |",
        "|------|-----------|-----------|--------|",
    ])
    L.append("")

    with open(ea, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")

    if com_conceitos:
        for nome in sorted(conceitos):
            escrever_conceito(vault, nome, conceitos[nome],
                              sorted(evidencias.get(nome, [])))

    print(f"estado-atual regenerado: {ea} "
          f"({len(conceitos)} conceitos, {len(erros)} com erro)")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--conceitos"]
    com_conceitos = "--conceitos" in sys.argv
    if len(args) != 1:
        print("uso: python recalcular-estado.py <vault> [--conceitos]")
        sys.exit(1)
    main(args[0], com_conceitos)
