# Fase 2 — Especificação

**Objetivo:** transformar cada RF em critérios de aceite verificáveis e cada RNF
em medida concreta.

> **Agnóstica de tecnologia.** (mesma regra da Fase 1)

## Seções

**Funcionalidades (derivadas dos RF)**
| RF | Funcionalidade | Status | Origem |

**Critérios de aceite por RF** — formato Dado/Quando/Então (Gherkin):
```
RF-01:
  Dado [contexto inicial]
  Quando [ação]
  Então [resultado esperado]
```

**Medidas por RNF**
| RNF | Categoria | Medida (limiar) | Como medir | Status | Origem |

**Fluxos de usuário (UX)**
| Fluxo | Jornada (passos) | Critério de usabilidade | Status | Origem |
> Wireframes de baixa fidelidade podem ser referenciados (opcional).

**Cenários de exceção/erro**
- ex.: fonte indisponível, token expirado, entrada inválida.

**Dependências e priorização**
- o que depende de quê; ordem de implementação.

## Definição de pronto

- [ ] cada RF com critérios de aceite em Dado/Quando/Então
- [ ] cada RNF com medida verificável (limiar + como medir)
- [ ] fluxos de usuário principais levantados, com critério de usabilidade
- [ ] cenários de exceção levantados
- [ ] nenhuma decisão de tecnologia no documento
- [ ] todo item com Origem rastreável (rigor)
- [ ] nenhum item sem suporte na auditoria (rigor)
- [ ] usuário validou item a item (rigor)
