# O sistema — manifesto e decisões

> O "porquê" do sistema. Os `00-visao-geral` documentam o *o quê/como*; este
> arquivo guarda as **razões** das escolhas — pro futuro-você evoluir sem perder
> o contexto original.

## Por que ele existe

Guiar o desenvolvimento e o estudo **assistidos por IA** com **rigor**, e
consolidar tudo numa **base de conhecimento** que vire um RAG pessoal (o
`personalrag` indexaria esse corpo).

O problema-raiz: **IA alucina** e interpreta requisitos de formas diferentes.
O sistema reduz esse espaço com **spec**, **rigor** e **rastreabilidade**.

## Princípios

1. **Fontes da verdade únicas** — molde canônico em `.opencode/templates/`, não
   duplicado nos agentes.
2. **Derivar, não manter à mão** — o que dá pra calcular, se calcula.
3. **Rastreabilidade mecânica** — links, não texto de confiança.
4. **Estrutura dirigida pelas consultas** — organiza pelo que se vai perguntar.
5. **RAG-friendly** — frontmatter, headings, sem duplicação.

## Decisões (ADR)

### D-01 — Rigor em 4 camadas (antes da automação)
- **Contexto:** instrução "soft" ("não invente") falha na prática.
- **Decisão:** contrato de escrita (`Status`/`Origem`), confirmação de paráfrase,
  auditoria de rastreabilidade, gate humano.
- **Descartou:** confiar só no prompt.
- **Motivo:** instrução não é mecânica; precisa de estrutura + verificação.

### D-02 — Event-sourcing (estado é derivado)
- **Contexto:** manter a matriz/estado à mão duplicava e divergia.
- **Decisão:** o log (observações/avaliações) é a fonte; o estado é **calculado**
  (`recalcular-estado.py`).
- **Descartou:** editar o `estado-atual` manualmente.
- **Motivo:** menos cerimônia; o estado nunca fica desatualizado.

### D-03 — Centrar no conceito (script + backlinks)
- **Contexto:** a info de um conceito ficava espalhada (dicionário, matriz, destilado).
- **Decisão:** uma **nota por conceito** — definição/sinônimos/pré-requisitos
  (manual) + nível/evidências (derivados pelo script); sessões usam `[[conceito]]`.
- **Motivo:** "o que sei sobre X?" vira uma nota só; chunk autocontido pro RAG.

### D-04 — Proveniência por links, não coluna de texto
- **Decisão:** a coluna `Origem` é um `[[link]]`, não texto livre.
- **Motivo:** a rastreabilidade vira **mecânica** (grafo do Obsidian), não confiança.

### D-05 — Dois tipos: `estudo` e `desenvolvimento`
- **Decisão:** mentor (ensina) vs engenheiro (entrega); `base.md` + `modo-*.md`.
- **Motivo:** papéis diferentes; e a base única acaba com a dupla manutenção.

### D-06 — Vault do projeto + vault do orquestrador
- **Decisão:** cada projeto **autocontido** (`doc/vault/`); o orquestrador tem um
  vault global que consolida via `sync`.
- **Motivo:** documentação junto do projeto + visão global (habilidade é do aluno).

### D-07 — Escalas Bloom (conceito) + Dreyfus (global)
- **Decisão:** Bloom mede profundidade por conceito; Dreyfus, o estágio geral.
- **Descartou:** autonomia 1–5 sozinha (não mede profundidade).
- **Motivo:** "saber fazer" ≠ "saber que sabe"; queríamos profundidade.

### D-08 — Progressão em 3 partes
- **Decisão:** Observabilidade (fatos) → Avaliação (medida) → Progressão (ação).
- **Motivo:** **separar fatos de juízo de ação**; misturar contamina a medida.

### D-09 — SDD: spec viva por feature
- **Decisão:** cada feature tem `specs/<feature>.md` (Spec + Plano + Tarefas).
- **Descartou:** só fases macro.
- **Motivo:** spec é contrato antes do código (corta alucinação); o **histórico da
  spec** vira a trajetória.

### D-10 — `historico/` invertida (datas primeiro)
- **Decisão:** `historico/YYYY/mm/<tipo>/`.
- **Motivo:** a **linha do tempo vem de graça** (abre o mês, vê tudo).

### D-11 — Estudo e dev juntos na pasta `progresso/`, separados por sufixo
- **Decisão:** `progresso/YYYY_mm_dd_prog.md` (estudo) e `_dev.md` (dev).
- **Motivo:** mesmo papel (registro da sessão); evitar dois nomes parecidos
  (`progresso`/`andamento`).

### D-12 — Bugs mistos; patterns para reuso
- **Decisão:** bug grande/médio = nota; menor = lote mensal. Solução reutilizável
  = `patterns/`.
- **Motivo:** separar **conserto pontual** de **solução repetível**.

### D-13 — Glossário (vocabulário controlado)
- **Decisão:** nome canônico + sinônimos; `conceitos/<nome>.md` + `_glossario.md`.
- **Motivo:** sem ele o mesmo conceito vira 3 na matriz (`mutável`/`mutability`).

## O que ainda é dúvida

- **Cerimônia:** o custo por sessão ainda pode ser alto.
- **Rigor é "soft":** falta um verificador independente (revisor).
- **Ainda não testado** de ponta a ponta; e falta migrar os projetos antigos.
