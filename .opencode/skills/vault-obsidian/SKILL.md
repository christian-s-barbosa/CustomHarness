---
name: vault-obsidian
description: Define o molde canônico do Obsidian vault usado nos projetos de C:\Users\chris\Projetos (nos moldes do FeedHub). Use ao criar/bootstrapar o doc/vault de um projeto, verificar se um vault segue o padrão, ou replicar o molde das fases, o sistema de progressão e a config .obsidian. Trigger keywords: vault, obsidian, doc/vault, bootstrap vault, moldar vault, criar vault, molde das fases, templates/fases, esqueleto-fase, estado-atual, observacoes, avaliacao, progresso, templates/progressao, core-plugins, engenharia-software, historico.
---

# Vault Obsidian — molde FeedHub

Fonte única de verdade da estrutura de documentação (Obsidian vault) que todo
projeto de `C:\Users\chris\Projetos` deve ter. O projeto de referência é o
`FeedHub`.

## Estrutura canônica

A base é a mesma; o que muda por **tipo** é o conteúdo de `historico/` e o
`estado-atual.md`:

```
<projeto>/doc/vault/
├── .obsidian/                 # config do Obsidian (não editar manualmente)
│   ├── app.json               # {}
│   ├── appearance.json        # {}
│   ├── core-plugins.json      # plugins habilitados (ver abaixo)
│   └── workspace.json         # layout (opcional; o Obsidian regenera)
├── anotacoes/                 # notas livres
├── engenharia-software/       # ciclo de vida, fases 00–08
├── specs/<feature>.md         # SDD: spec viva por feature (o quê + plano + tarefas)
├── design/DESIGN.md           # sistema visual (UI) — fonte da verdade do visual
├── bugs/<slug>.md             # bug grande/médio (nota própria)
├── bugs/menores-YYYY_MM.md    # bugs menores (lote mensal)
├── patterns/<slug>.md         # soluções reutilizáveis (reuso)
├── historico/YYYY/mm/...      # sessões (datas primeiro; ver variante por tipo)
├── estado-atual.md            # ver variante por tipo
└── templates/                 # cópias dos moldes
```

**Tipo `estudo` (mentor):**
- `historico/YYYY/mm/observacoes/YYYY_mm_dd.md`
- `historico/YYYY/mm/avaliacao/YYYY_mm_dd.md`
- `historico/YYYY/mm/progresso/YYYY_mm_dd_prog.md`
- `historico/retrospectivas/fase-N.md`
- `estado-atual.md` → painel de **habilidades do aluno**
- moldes: `.opencode/templates/progressao/`

**Tipo `desenvolvimento` (engenheiro):**
- `historico/YYYY/mm/progresso/YYYY_mm_dd_dev.md`
- `estado-atual.md` → estado do **projeto**
- moldes: `.opencode/templates/andamento/`

> Os moldes (fases, progressão, andamento) **não ficam no vault** — são canônicos
> no workspace, em `.opencode/templates/`. Veja as seções "Molde das fases
> (canônico)" e "Sistema de progressão (canônico)".

## Bootstrap (projeto sem vault)

Quando um projeto **não tiver** `doc/vault/`, crie o esqueleto mínimo abaixo:

1. Pastas: `doc/vault/.obsidian/`, `doc/vault/anotacoes/`,
   `doc/vault/engenharia-software/`, `doc/vault/specs/`, `doc/vault/design/`,
   `doc/vault/bugs/`, `doc/vault/patterns/`, `doc/vault/historico/`,
   `doc/vault/templates/`.
2. `doc/vault/.obsidian/app.json` → `{}`
3. `doc/vault/.obsidian/appearance.json` → `{}`
4. `doc/vault/.obsidian/core-plugins.json` → JSON da seção "core-plugins.json".
5. `doc/vault/engenharia-software/00-perguntas-em-aberto.md` → frontmatter
   `titulo` / `tipo: indices` / `status: em uso` + header (ver seção abaixo).
6. **Específico por tipo:**
   - **`estudo`:** `estado-atual.md` = molde `.opencode/templates/progressao/estado-atual.md`;
     `templates/` = cópias de `.opencode/templates/progressao/`.
   - **`desenvolvimento`:** `estado-atual.md` = molde `.opencode/templates/andamento/estado-atual.md`;
     `templates/` = cópias de `.opencode/templates/andamento/`.
7. `doc/vault/index.md` → gere o MOC (ligado a **todas** as notas) com o script:
   ```
   powershell -NoProfile -ExecutionPolicy Bypass -File "C:\Users\chris\Projetos\.opencode\scripts\gerar-index.ps1" -VaultPath "<vault do projeto>" -Titulo "<nome do projeto>"
   ```

> As fases numeradas `01`–`08` e os registros de `historico/` **não** são criados
> no bootstrap. As fases nascem ao concluir cada etapa (molde
> `.opencode/templates/fases/`); os registros, ao fim de cada sessão (skill
> `encerrar-sessao`, molde `.opencode/templates/progressao/`). O bootstrap só
> prepara o esqueleto + templates + índice.

## Regras

- Não invente estrutura nova; siga exatamente este molde.
- O `doc/vault` **vai pro git junto com o projeto** (é o backup/versionamento).
  Opcional: manter `.obsidian/workspace.json` (estado de UI) fora do git.
- `workspace.json` é opcional no bootstrap (estado de UI do Obsidian).
- **Índice (`index.md`):** mapeia **todas** as notas (incluindo `historico/` e
  `engenharia-software/`), exceto `.obsidian/` e `templates/`. Regenerar sempre
  que notas forem criadas/alteradas (script `gerar-index.ps1`).
- Ao "moldar" um vault existente mas incompleto, complete o que falta sem
  reescrever conteúdo já existente.

## `core-plugins.json`

```json
{
  "file-explorer": true,
  "global-search": true,
  "switcher": true,
  "graph": true,
  "backlink": true,
  "canvas": true,
  "outgoing-link": true,
  "tag-pane": true,
  "footnotes": false,
  "properties": true,
  "page-preview": true,
  "daily-notes": true,
  "templates": true,
  "note-composer": true,
  "command-palette": true,
  "slash-command": false,
  "editor-status": true,
  "bookmarks": true,
  "markdown-importer": false,
  "zk-prefixer": false,
  "random-note": false,
  "outline": true,
  "word-count": true,
  "slides": false,
  "audio-recorder": false,
  "workspaces": false,
  "file-recovery": true,
  "publish": false,
  "sync": true,
  "bases": true,
  "webviewer": false
}
```

## `00-perguntas-em-aberto.md` (esqueleto de bootstrap)

```markdown
---
titulo: Perguntas em Aberto
tipo: indices
status: em uso
---

# Perguntas em Aberto (decidir / documentos)

> Índice central das decisões pendentes do <projeto>. Cada fase/doc de
> engenharia referencia este arquivo em vez de duplicar as perguntas.
> `Resolvida` = já decidida. `Aberta` = aguarda decisão.

## Abaixo — todas as pendências

<!-- Ex.: ### PQ-01 — <título> / - Status / - Impactos / - Decisão -->
```

## Molde das fases (canônico)

O template por fase **não** é mais um único `engenharia-fase.md` genérico. O
molde canônico está em `.opencode/templates/fases/`:

- `00-visao-geral.md` — as 8 fases, o protocolo de rigor (4 camadas) e as regras globais.
- `esqueleto-fase.md` — o casco comum às 8 fases.
- `fase-01-requisitos.md` ... `fase-08-manutencao.md` — o guia de cada fase
  (seções + definição de pronto), incluindo os formatos da Fase 3
  (`just-enough` / `adr` / `c4`) e da Fase 5 (`por-feature` / `diario` / `por-sprint`).

Ao criar/atualizar um documento de fase no vault, siga esse molde (esqueleto
comum + o guia da fase) e aplique o protocolo de rigor: colunas `Status`/`Origem`
nas tabelas, auditoria de rastreabilidade antes de validar e gate humano
(readback item a item) antes de `status: validado`.

## Sistema de progressão (canônico)

O sistema de progressão (3 partes) é canônico em `.opencode/templates/progressao/`:

- `00-visao-geral.md` — o pipeline (Observabilidade → Avaliação → Progressão), escalas e regras.
- `observacao.md` — fatos brutos da sessão.
- `avaliacao.md` — medida de habilidade (Bloom por conceito + Dreyfus global).
- `progresso.md` — controle (onde estamos, próximos passos, ajuste de postura).
- `estado-atual.md` — cumulativo vivo (matriz, erros recorrentes, lacunas, metas, revisão espaçada).

Os registros vivem em `doc/vault/historico/{observacoes,avaliacao,progresso}/YYYY/mm/`
e o painel em `doc/vault/estado-atual.md`. Ao fim de cada sessão, a skill
`encerrar-sessao` produz as 3 partes e atualiza o `estado-atual.md`.
