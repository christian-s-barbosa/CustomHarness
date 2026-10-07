---
tipo: observacao
projeto: <projeto>
data: YYYY-MM-DD
sessao: N
fase: N
conceitos: []
erros: []
---

# Observação — YYYY-MM-DD

## Contexto
- Fase: N — <nome> · Tema: <conceito/tema em jogo>

## Eventos (fatos brutos)
| # | Conceito | Evento | Sozinho? |
|---|----------|--------|----------|
| 1 | [[<conceito>]] | <errou / acertou / dúvida — o fato> | sim / não / — |

## Notas
- <o que foi feito, o que ficou pendente>

<!-- Regra: só FATOS (sem juízo).
     Frontmatter é o dado estruturado: `conceitos` (tocados) e `erros` (onde errou),
     usados pelo recalcular-estado.py. No corpo, referencie o conceito como
     [[conceito]] — isso gera o backlink no Obsidian (ideia A+B). -->
