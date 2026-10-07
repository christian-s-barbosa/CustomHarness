# Backlog — ideias a analisar depois

Coisas que avaliamos mas **não** adotamos agora. Ficam aqui pra decidir depois.
(Os repositórios foram clonados em `%TEMP%\opencode\repos\` para inspeção.)

## Do ECC (`affaan-m/ECC`) — não adotado como harness

Não colocamos o ECC inteiro (55 MB, 293 skills, 68 agentes — brigaria com nosso
sistema e inflaria o contexto). Extraímos só o `santa-method` → **`revisor`** e o
`verification-loop` → **`verificar`**. O resto:

- **`eval-harness`** — eval-driven development: define evals (capability/regression)
  antes de codar e mede `pass@k`/`pass^k`. *Overkill* para uso solo; valeria se
  fossemos comparar modelos/prompts ou montar suíte de regressão de agente.
- **`strategic-compact`** — sugere compactar o contexto em **fronteiras lógicas**
  (depois de explorar, antes de executar). O opencode já tem compactação própria
  (`compaction` no config); a *ideia* pode virar regra nossa.
- **`unified-memory`** — vault de memória entre harnesses (docs `ecc.memory.v1`,
  escopos project/team/user, CLI+MCP). **Sobrepõe o nosso vault**; vale como
  *inspiração de formato*. Exige runtime `ecc-universal` (npm). Insight bom:
  *"recall é evidência, não certeza"*.
- **AgentShield** — scanner (npm `ecc-agentshield`) que audita a **config do
  agente** (AGENTS.md, MCP, hooks, permissões, secrets). É uma **lacuna nossa**
  (segurança da própria config) — *nice-to-have*.

## Do GSD (`gsd-build/get-shit-done` → ativo: `open-gsd/gsd-core`)

Spec-driven + context-engineering. Ideias de alto valor, ainda não implementadas:

- **Gate de ambiguidade** — entrevista com *score* quantificado; só passa se a
  ambiguidade ≤ 0.20. (Plugar no Passo 2 do fluxo spec-first.)
- **`CONTEXT.md` + `canonical_refs`** — separar o QUÊ do COMO e exigir os caminhos
  que os subagentes *devem* ler (alavanca anti-alucinação).
- **Provenance** — marcar `[VERIFIED]/[CITED]/[ASSUMED]`; a `ASSUMED` vira gate
  humano.
- **Anti-pattern scan** — bloquear `TBD/FIXME/placeholder/return null` no verificar.
- **Test-quality audit** — detectar testes circulares/desabilitados.
- **Verify goal-backward** — `must_haves` no plano; verifica *objetivo*, não *tarefa*.

## Do Graphify (`Graphify-Labs/graphify`)

Grafo de conhecimento de código+docs, consultável.

- **MCP** `query_graph`/`shortest_path`/`get_node`; integra **nativo no opencode**;
  arestas `EXTRACTED/INFERRED`; roda local (`--backend ollama`).
- Uso: camada **opcional** de compreensão sobre o vault (RAG *estrutural*, grafo
  em vez de embeddings). Custo: médio. *Não* substitui nosso `sync`/vault.

## Já adotados (referência)

- `ui-ux-pro-max` (skill) + `DESIGN.md` (molde) — UI/UX.
- `santa-method` → `revisor`; `verification-loop` → `verificar`.
