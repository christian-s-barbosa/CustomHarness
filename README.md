# CustonHarness

> Harness customizado sobre o [opencode](https://opencode.ai) — uma camada que
> organiza **vários projetos** (cada um com um vault Obsidian) e os consolida num
> **vault global** que vira uma base de conhecimento (RAG) no futuro.

## O que é

Uma configuração de harness que guia o **desenvolvimento e o estudo assistidos
por IA** com rigor, rastreabilidade e spec-driven development. Feito sobre os
primitivos do opencode (agentes, skills, templates, scripts).

## Componentes

- **Agentes:** `orquestrador` (analisa e consolida os projetos) + subagentes.
- **Skills:** `criar-projeto`, `vault-obsidian`, `sync`, `ui-ux-pro-max`,
  `revisor` (verificação adversarial), `verificar` (verificação determinística),
  `git-flow`, entre outras.
- **Templates:** fases de engenharia (8), progressão (estudo), andamento (dev),
  conceitos, specs (SDD), design, bugs, patterns.
- **Scripts:** `gerar-index.ps1` (índice do vault), `recalcular-estado.py`
  (event-sourcing: o estado é derivado do log).
- **Dois tipos de projeto:** `estudo` (mentor) e `desenvolvimento` (engenheiro).

## Estrutura

```
.opencode/     agentes, skills, scripts e templates (molde canônico)
doc/vault/     vault do orquestrador (base de conhecimento consolidada)
opencode.json  config (default_agent: orquestrador)
```

## Referências

- `SISTEMA.md` — o **porquê** das decisões de design.
- `BACKLOG.md` — ideias avaliadas e adiadas para depois.

## Licença

MIT — veja `LICENSE`.
