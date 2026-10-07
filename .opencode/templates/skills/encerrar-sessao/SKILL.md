---
name: encerrar-sessao
description: Use when a mentoring session ends (user says "/ends", "fim de sessão", "encerrar", "até logo" or asks to registrar progresso). Produces the 3 progression parts (observação, avaliação, progresso) and updates estado-atual.md, following the templates in .opencode/templates/progressao/. Trigger keywords: fim de sessão, encerrar, progresso, observação, avaliação, registrar sessão, histórico.
---

# Encerrar sessão — registrar progresso

Ao fim de cada sessão de mentoria, produza as **3 partes** do sistema de
progressão e atualize o `estado-atual.md`. Siga os templates canônicos em
`.opencode/templates/progressao/` (`00-visao-geral.md`, `observacao.md`,
`avaliacao.md`, `progresso.md`, `estado-atual.md`).

## Pipeline

```
Observabilidade  →  Avaliação  →  Progressão
(fatos)             (medida)      (ação)
```

## Passos

### 1. Observabilidade
Leia o template `observacao.md`. Registre os **FATOS** da sessão:
- **Contexto:** fase/tema em jogo.
- **Eventos:** por conceito — o que aconteceu (erro/acerto/dúvida) e se foi sozinho.
- **Notas:** o que foi feito, o que ficou pendente.

Preencha o **frontmatter**: `conceitos` (tocados) e `erros` (onde errou) — usados
pelo `recalcular-estado.py`.

Sem juízo de valor. Salve em
`doc/vault/historico/YYYY/mm/observacoes/YYYY_mm_dd.md` (crie a pasta se faltar).

### 2. Avaliação
Leia o template `avaliacao.md`. **Pergunte ao aluno** (uma coisa por vez):
- auto-avaliação global (Dreyfus) + justificativa;
- confiança por conceito tocado.

Preencha o **frontmatter** (dado estruturado):
- `dreyfus` (auto-avaliação + a sua, com discordância);
- `conceitos[]` com `nome`, `nivel` (Bloom), `evidencia` e `confianca`.

No corpo, escreva a **leitura do mentor** (dificuldades/padrões) e a discordância.

Salve em `doc/vault/historico/YYYY/mm/avaliacao/YYYY_mm_dd.md`.

> **Discordância:** registre confiança (aluno) e competência (você, com evidência).
> Só reconcilie quando o **gap for grande**; sem evidência conclusiva, marque
> **"em disputa"** e colete mais na próxima sessão. O ajuste de postura segue a
> **competência medida**.

### 3. Progressão
Leia o template `progresso.md`. Registre:
- **onde estamos** (fase, foco atual);
- **próximos passos**;
- **ajuste de postura** (perguntar mais / confirmar mais, conforme o nível).

Salve em `doc/vault/historico/YYYY/mm/progresso/YYYY_mm_dd_prog.md`.

### 4. Recalcular o `estado-atual.md`
O estado é **derivado** das observações/avaliações (event-sourcing). Não edite a
matriz à mão — rode o script:
```
python "C:\Users\chris\Projetos\.opencode\scripts\recalcular-estado.py" "<vault do projeto>"
```
As seções derivadas (Dreyfus, matriz, confiança, erros, revisão, lacunas) são
geradas. Depois, se necessário, preencha a seção manual **Metas**.

### 5. Regenerar o índice (MOC)
Regenere o `index.md` do vault (ligado a **todas** as notas):
```
powershell -NoProfile -ExecutionPolicy Bypass -File "C:\Users\chris\Projetos\.opencode\scripts\gerar-index.ps1" -VaultPath "<vault do projeto>" -Titulo "<nome do projeto>"
```

### 6. Evitar sobrescrever
Se o arquivo do dia já existir, anexe sufixo: `_2`, `_3`, etc.

### 7. Confirmar
Mostre os caminhos salvos (observação, avaliação, progresso, estado-atual, index)
e um resumo de 1 linha do que ficou registrado.

## Regras

- **Observabilidade = só fatos.** Juízo ("foi bem", "tem dificuldade") vai na Avaliação.
- **Avaliação: toda medida cita evidência.** Sem evidência = sem nível.
- **Pergunte, não invente** (auto-avaliação, confiança, metas).
- Não altere os templates canônicos.
