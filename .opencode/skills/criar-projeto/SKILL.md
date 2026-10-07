---
name: criar-projeto
description: Cria um novo projeto em C:\Users\chris\Projetos a partir de uma entrevista. Pergunta nome, tipo de agente (estudo | desenvolvimento), propósito, stack e remoto, e gera o esqueleto: AGENTS.md conforme o tipo (templates em .opencode/templates/agentes/), vault Obsidian em doc/vault no molde FeedHub e as skills/agentes do tipo. Use when the user says "criar projeto", "novo projeto", "scaffold projeto", "iniciar projeto". Trigger keywords: criar projeto, novo projeto, scaffold, bootstrap projeto, iniciar projeto.
---

# Criar projeto

Cria um novo projeto em `C:\Users\chris\Projetos` a partir de uma entrevista com
o usuário.

## Tipos de agente

- **`estudo`** — mentor: ensina (socrático), trava de escrita e registra o
  progresso de **aprendizado** (histórico de mentoria).
- **`desenvolvimento`** — engenheiro: implementa e documenta, **sem** socrático e
  **sem** trava de escrita; registra o **andamento do projeto**.

## Passo 1 — Entrevista (uma coisa por vez)

Pergunte e colete **todas** as respostas antes de criar. Não invente respostas.

1. **Nome** do projeto (pasta a criar em `C:\Users\chris\Projetos\`).
2. **Tipo de agente** → `estudo` | `desenvolvimento`.
3. **Propósito** (1–2 linhas: o que é / o que se estuda ou constrói).
4. **Stack/linguagem** (ex.: `Python`, `Python/OOP`, `JavaScript/Node`).
5. **Repositório remoto** (opcional; ex.: `usuario/repo`).
6. **Licença** (opcional; default `MIT`).

## Passo 2 — Gerar a estrutura

Crie a pasta `C:\Users\chris\Projetos\<nome>` e o conteúdo abaixo.

### 2.1 AGENTS.md (composto de base + modo)

O AGENTS.md é montado de **dois** arquivos (fonte única = sem duplicação):

1. Leia:
   - `.opencode/templates/agentes/base.md` — os pontos comuns (processo, fluxo);
   - `.opencode/templates/agentes/modo-<tipo>.md` — o específico
     (`modo-estudo.md` ou `modo-desenvolvimento.md`).
2. Monte o conteúdo:
   - substitua `{{ESPECIFICO}}` no base pelo **conteúdo do modo**;
   - demais placeholders:
     - `{{PAPEL}}` → `Mentor sênior` (estudo) | `Engenheiro sênior` (desenvolvimento);
     - `{{STACK}}` → stack informada;
     - `{{NOME}}` → nome do projeto;
     - `{{CONTEXTO}}` → bloco de contexto (ver formato abaixo);
     - `{{PENDENCIAS}}` → pendências iniciais (ver formato abaixo).
3. Grave em `<nome>/AGENTS.md`.

Formato do bloco de contexto (`{{CONTEXTO}}`):
```
- Projeto: `<nome>` — <propósito>.
- Estado atual: repositório recém-criado, ainda sem código.
- Stack: <stack>.
- Remoto: <repo | —>.
- Documentação/anotações: Obsidian vault em `doc/vault/` (vai pro git junto com o projeto).
- Licença: <licença>.
```

Formato das pendências iniciais (`{{PENDENCIAS}}`) — ajuste conforme o propósito:
```
- Definir o que o projeto vai entregar (Fase 1 — Requisitos).
- Definir a estrutura de pastas/módulos e a gerência de dependências.
- Definir testes e ferramentas de qualidade (lint/type-check).
```

### 2.2 Vault `doc/vault`

Siga a skill **`vault-obsidian`** (bootstrap conforme o **tipo**). Inclua:
- `.obsidian/` (`app.json`, `appearance.json`, `core-plugins.json`);
- `anotacoes/`, `historico/`, `specs/`, `design/`, `bugs/` e `patterns/` (vazias);
- `engenharia-software/00-perguntas-em-aberto.md`;
- `estado-atual.md` + `templates/` conforme o tipo:
  - `estudo` → moldes de `.opencode/templates/progressao/`;
  - `desenvolvimento` → moldes de `.opencode/templates/andamento/`.

Os documentos de fase (`engenharia-software/0N-*.md`) seguem o molde canônico em
`.opencode/templates/fases/` (`esqueleto-fase.md` + `fase-0N-*.md`) — ver a skill
`vault-obsidian`.

### 2.3 Skills do projeto

Copie os moldes de `.opencode/templates/skills/` para `<nome>/.opencode/skills/`:
- **comuns (ambos os tipos):** `git-flow` (versionamento), `revisor` (verificação adversarial), `verificar` (verificação determinística).
- **`estudo`:** `encerrar-sessao`, `diagnostico-inicial`, `retrospectiva-fase`.
- **`desenvolvimento`:** `registrar-andamento`.

Copie também a skill **`ui-ux-pro-max`** de `.opencode/skills/ui-ux-pro-max/` para
`<nome>/.opencode/skills/ui-ux-pro-max/` (UI/UX — sistema visual).

### 2.4 Sub-agente (só `desenvolvimento`)

Copie `.opencode/templates/agentes/fase-engenharia.md` para
`<nome>/.opencode/agent/fase-engenharia.md`.

### 2.5 Marcador de tipo

Copie `.opencode/templates/projeto/marcador.md` para `<nome>/.opencode/projeto.md`,
substituindo `<projeto>` pelo nome e `tipo:` pelo tipo escolhido.

## Passo 3 — Confirmar

Mostre ao usuário um resumo do que foi criado (pastas/arquivos) e as pendências
iniciais sugeridas.

## Regras

- Crie o projeto **somente** depois de coletar todas as respostas da entrevista
  (uma por vez, sem assumir).
- O `doc/vault` **vai pro git junto com o projeto** (backup/versionamento).
- Não crie commits nem inicialize git automaticamente.
