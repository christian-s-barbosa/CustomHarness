---
name: diagnostico-inicial
description: Use on the first session of a project (when estado-atual.md is empty or absent) to establish a baseline. Guides a short diagnostic (prior experience + probing key concepts) and seeds estado-atual.md and the concept glossary instead of starting "tudo nível 0". Trigger keywords: primeira sessão, diagnóstico inicial, onboarding, baseline, estado-atual vazio.
---

# Diagnóstico inicial — semear o estado-atual

Use quando o projeto **não tiver histórico** (o `doc/vault/estado-atual.md`
estiver vazio ou ausente). Objetivo: estimar um **baseline** em vez de começar
"tudo nível 0".

## Passos

1. **Conversa inicial** (socrático, uma pergunta por vez):
   - experiência prévia com a stack;
   - o que já sabe / o que quer aprender;
   - como prefere trabalhar.

2. **Sondagem de conceitos.** Escolha 3–5 conceitos-chave do domínio do projeto e
   faça **perguntas ou tarefas curtas** para estimar o nível Bloom de cada um. Uma
   coisa por vez; deixe o aluno prever antes de responder.

3. **Registrar uma avaliação inicial** (evento). Escreva
   `doc/vault/historico/YYYY/mm/avaliacao/YYYY_mm_dd.md` com os níveis estimados
   no **frontmatter** (`conceitos[]` com `nivel`), marcando hipóteses na evidência
   ("hipótese — a confirmar"). Depois rode `recalcular-estado.py` para gerar o
   `estado-atual.md`.

4. **Anotar os conceitos** identificados (nome + sinônimos + categoria +
   pré-requisitos) — o `sync` os levará ao glossário global
   `conceitos/_glossario.md`.

5. **Regenerar o índice** (MOC, ligado a todas as notas) com o script
   `gerar-index.ps1`.

6. **Confirmar.** Mostre a matriz inicial e um plano de aprendizado curto.

## Regras

- Não invente níveis: toda estimativa é **hipótese** até a primeira avaliação real.
- Uma coisa por vez; método socrático (ver AGENTS.md).
- O diagnóstico **semeia**; a `encerrar-sessao` (ao fim da 1ª sessão) refina.
