# Sistema de progressão — visão geral

Fonte canônica do sistema de progressão do aluno. Funciona como um pipeline:

```
Observabilidade  →  Avaliação  →  Progressão
(o que aconteceu)   (quão bom)     (para onde vamos)
   fatos brutos      medida          ação
        ↑___________________________________|
              (o foco realimenta a observação)
```

## As 3 partes

1. **Observabilidade** — registro bruto (fatos) da sessão. Sem juízo.
2. **Avaliação** — medida de habilidade, derivada das observações. Com juízo.
3. **Progressão** — controle: onde estamos, foco, próximos passos, ajuste de postura.

## Artefatos (no vault do projeto)

- `historico/YYYY/mm/observacoes/YYYY_mm_dd.md` — observabilidade (por sessão)
- `historico/YYYY/mm/avaliacao/YYYY_mm_dd.md` — avaliação (snapshot por sessão)
- `historico/YYYY/mm/progresso/YYYY_mm_dd_prog.md` — progressão (snapshot por sessão)
- `estado-atual.md` — **derivado** (gerado pelo `recalcular-estado.py` a partir das observações/avaliações)

## Escalas

- **Bloom (por conceito):** `Lembrar · Entender · Aplicar · Analisar · Avaliar · Criar`
- **Dreyfus (global):** `Novato · Iniciante avançado · Competente · Proficiente · Especialista`

## Regras

- **Observabilidade:** só fatos (o que foi feito, onde travou, se foi sozinho). Sem juízo.
- **Avaliação:** toda medida **cita evidência** (o evento da observação). Avaliação **mista** (auto + mentor), com discordância explícita.
- **Revisão espaçada** (por nível Bloom):
  - `Lembrar / Entender` → 1–3 dias
  - `Aplicar / Analisar` → ~1 semana
  - `Avaliar / Criar` → 2–4 semanas

## Discordância (auto-avaliação × mentor)

- Registrar **sempre os dois**: *confiança* (aluno) + *competência* (mentor, com evidência).
- O **ajuste de postura** segue a **competência medida** (não a auto-percepção).
- **Reconciliar só quando o gap é grande** (não toda sessão).
- Gap grande → o mentor **mostra a evidência** e convida a reflexão (sem decretar).
- **Evidência nova** (do aluno, fora da sessão) → o mentor **atualiza**.
- **Sem evidência conclusiva** → marcar **"em disputa"** e coletar mais na próxima sessão.
- A **matriz usa a competência**; a confiança é preservada como dado de **calibração**.

## Estado cumulativo (`estado-atual.md`) — event-sourcing

O estado é **derivado** das observações/avaliações, não editado à mão. O log é a
fonte da verdade (append-only); o `estado-atual.md` é a **projeção calculada**:

```
python recalcular-estado.py <vault>
```

- **Derivado (recalculado):** Dreyfus, matriz de habilidades, confiança ×
  competência, erros recorrentes, revisão espaçada e **lacunas de pré-requisitos**
  (pré-requisitos das notas de conceito abaixo do limiar).
- **Manual (preservado):** metas.

O dado estruturado fica no **frontmatter** de cada evento (`conceitos[]` com
`nivel`/`evidencia`/`confianca`, `erros[]`, `dreyfus`) — o corpo é prosa.

## Global (orquestrador)

O vault do orquestrador (`Projetos/doc/vault/`) consolida tudo via a skill
**`sync`**: espelha o cru (`historico/<projeto>/`) e destila
(`conceitos/`, `projetos/`, `decisoes/`) — base de conhecimento para um futuro RAG.
