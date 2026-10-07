---
name: sync
description: Use when consolidating the project vaults into the orchestrator's knowledge base (user says "sync", "sincronizar", "consolidar vaults", "atualizar o vault do orquestrador"). Mirrors the raw project vault content into historico/<projeto>/ and distills it into conceitos/, projetos/ and decisoes/, updating the global estado-atual.md. Runs on demand. Trigger keywords: sync, sincronizar, consolidar, vault do orquestrador, base de conhecimento, estado global.
---

# sync — consolidar os vaults no vault do orquestrador

Consolida os vaults dos projetos em `Projetos/doc/vault/` (base de conhecimento
do aluno, preparada para virar um RAG no futuro). Roda **sob demanda**.

## Onde está o quê

- **Vault do orquestrador:** `C:\Users\chris\Projetos\doc\vault\`
- **Vaults dos projetos:** `C:\Users\chris\Projetos\<projeto>\doc\vault\`

## Estrutura do vault do orquestrador

```
Projetos/doc/vault/
├── .obsidian/
├── index.md                     # MOC / home
├── estado-atual.md              # matriz GLOBAL de habilidades
├── conceitos/_glossario.md      # vocabulário controlado (canônico + sinônimos)
├── conceitos/<conceito>.md      # destilado (agrega evidências de todos os projetos)
├── projetos/<projeto>.md        # destilado (resumo + decisões + aprendizados)
├── decisoes/<projeto>/<ADR>.md
└── historico/<projeto>/...      # cru (espelho do vault do projeto)
```

## Passos

1. **Varrer os projetos** — liste as subpastas de `C:\Users\chris\Projetos\` que
   tenham `doc/vault/`. Ignore `.opencode`, `node_modules`, `doc` (do próprio
   orquestrador) e pastas ocultas.

2. **Espelhar o cru** — para cada projeto, copie **todo** o conteúdo do vault
   (exceto `.obsidian/` e `templates/`) para `doc/vault/historico/<projeto>/`.
   Isso inclui:
   - **estudo:** `historico/YYYY/mm/{observacoes,avaliacao,progresso}/`,
     `historico/retrospectivas/` e `estado-atual.md` (habilidades)
   - **desenvolvimento:** `historico/YYYY/mm/progresso/*_dev.md` e `estado-atual.md` (projeto)
   - **ambos:** `engenharia-software/` (docs das fases 00–08) e `anotacoes/`

3. **Derivar** (a partir do cru espelhado) — rode o script com `--conceitos`:
   ```
   python "C:\Users\chris\Projetos\.opencode\scripts\recalcular-estado.py" "C:\Users\chris\Projetos\doc\vault" --conceitos
   ```
   Isso gera o `estado-atual.md` global e as notas `conceitos/<nome>.md`
   (nível + evidências), preservando definição/sinônimos/pré-requisitos manuais.

   Depois, mantenha à mão (destilado):
   - **`conceitos/_glossario.md`** — o índice (lista de `[[conceito]]`).
   - **`projetos/<projeto>.md`** — resumo do projeto: propósito, stack, decisões
     principais e aprendizados — destilado dos `engenharia-software/` e do
     `estado-atual.md` do projeto.
   - **`decisoes/<projeto>/<ADR>.md`** — extraia os ADRs da
     `engenharia-software/fase-03` do projeto.

4. **Atualizar `estado-atual.md` global** — matriz consolidada: por conceito, o
   **maior nível Bloom** já atingido (habilidade não regride; no máximo fica
   "a revisar" se ficar tempo sem prática). Metas e revisão espaçada globais.
   > Alimentada pelos projetos de **`estudo`** (que têm a progressão de
   > aprendizado). Os de **`desenvolvimento`** contribuem com `projetos/` e
   > `decisoes/`, mas não com a matriz de habilidades.

5. **Regenerar `index.md`** (MOC, ligado a **todas** as notas) com o script:
```
powershell -NoProfile -ExecutionPolicy Bypass -File "C:\Users\chris\Projetos\.opencode\scripts\gerar-index.ps1" -VaultPath "C:\Users\chris\Projetos\doc\vault" -Titulo "Base de conhecimento - orquestrador"
```

## Regras RAG-friendly

- **Frontmatter** em todo doc: `tipo`, `projeto`, `conceitos`, `data`/`atualizado`, `nivel`.
- **Seções com headings claros** — o `personalrag` fatia por seção (chunk + breadcrumb).
- **Conceitos como tags**, referenciando o vocabulário global (`conceitos/`).
- **Sem duplicação** — destilar, não copiar. O cru fica em `historico/`.
- **Merge por conceito:** maior nível Bloom; **nunca rebaixar**.

## Confirmar

Mostre o que foi espelhado e destilado (projetos, conceitos, decisões) e o resumo
do estado global. Não sobrescreva destilados sem avisar.

## Nota

O `estado-atual.md` global é o "painel" do aluno. O vault do projeto continua
autocontido; este aqui é a **visão consolidada**.
