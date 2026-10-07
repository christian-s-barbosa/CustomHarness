# Instruções do projeto — {{PAPEL}} de {{STACK}}

{{ESPECIFICO}}

## Processo de Engenharia de Software

Ciclo de vida completo do {{NOME}}. As fases se desenrolam **nesta ordem**, sem
pular etapas. Retomar uma fase anterior só é válido se uma decisão da fase
seguinte exigir (é ida e volta, não quebra).

1. **Levantamento de Requisitos** — entender o que o projeto precisa fazer, para
   quem, e separar o essencial (MVP) do secundário. Registrado no vault.
2. **Especificação** — transformar requisitos em funcionalidades concretas e
   mensuráveis, com critérios de aceite claros.
3. **Arquitetura** — decisões técnicas de alto nível: stack, camadas, modelagem
   de dados e contratos de API. Cada decisão registra o **porquê**.
4. **Design de módulos** — detalhar cada parte em tipos, responsabilidades e
   interfaces. Ainda sem código.
5. **Desenvolvimento** — implementar seguindo o design. Cada feature usa o
   *Fluxo por Feature* abaixo.
6. **Testes de Qualidade** — estratégia de testes + ferramentas de qualidade
   (lint/type-check), até virar critério de "pronto".
7. **Implementação/Deploy** — colocar em produção: hospedagem, CI/CD, env vars e
   secrets.
8. **Manutenção** — corrigir e evoluir com base no uso, voltando às fases
   anteriores quando necessário.

Regras:
- Documentar cada fase no vault (decisões + racional), não só o produto.
- Requisitos bem definidos **antes** da arquitetura; arquitetura validada
  **antes** do desenvolvimento; testes como critério de "pronto".
- Quando um requisito/design estiver ambíguo, **perguntar** em vez de assumir.
- **Ao terminar cada fase**, gerar o doc em `doc/vault/engenharia-software/`
  seguindo o molde `.opencode/templates/fases/` (`esqueleto-fase.md` +
  `fase-0N-*.md`), **encadear** com a anterior/próxima (seção `## Navegação`) e
  **regenerar o índice** (`gerar-index.ps1`).

## Fluxo por Feature (spec-first)

Cada feature/refatoração percorre estas etapas, **uma por vez**. A **spec** é o
primeiro artefato e o contrato (Spec-Driven Development):

1. **Entender** — ler o contexto (README/vault) e aclarar objetivos.
2. **Escrever/atualizar a spec** — em `doc/vault/specs/<feature>.md`, com as 3
   partes: **Spec** (o quê), **Plano** (o como) e **Tarefas** (a quebra).
3. **Implementar** — seguindo a spec e as convenções do projeto.
4. **Verificar** — rode a skill **`verificar`** (testes + lint + type-check)
   **contra os critérios de aceite da spec**; para o gate semântico (anti-alucinação),
   a skill **`revisor`**.
5. **Revisar** — melhorar só o necessário (evitar "gold-plating").
6. **Validar a spec** — marcar `status: validado` e atualizar se algo mudou.

- A **spec é viva**: se o requisito muda, muda a spec primeiro.
- Cada tarefa tem um **definition of done** explícito.
- Se uma etapa "grande" aparecer, quebre em partes pequenas e validáveis.

## Versionamento (git-flow)

Siga a skill **`git-flow`** — GitHub Flow + Conventional Commits:
- Trabalhe em **branch curta** (`feat/`, `fix/`, `docs/`, `chore/`), **nunca** direto na `main`.
- Commits no formato `<tipo>: <descrição>`.
- **Mostre** o que vai commitar; **não** faça `push`/`merge` sem avisar; **nunca** versione segredo.

## Contexto do projeto

{{CONTEXTO}}

## Pendências atuais (o foco de melhorias)

{{PENDENCIAS}}
