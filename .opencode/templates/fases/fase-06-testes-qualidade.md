# Fase 6 — Testes de Qualidade

**Objetivo:** definir e executar a estratégia de testes + ferramentas de
qualidade até virar critério de "pronto". Aqui entra o **CD → HML** e os
**testes de acessibilidade**.

## Seções

**Estratégia de testes** — a pirâmide:
- unitários (base, muitos) → integração (meio) → e2e (topo, poucos).

**Matriz de testes**
| Teste | Tipo | RF/RNF coberto | Ferramenta | Status | Origem |

**Ferramentas de qualidade**
| Ferramenta | O que faz | Config | Status | Origem |
> lint, type-check, coverage, etc.

**Testes de acessibilidade** — rastreados ao RNF de Acessibilidade da Fase 1:
- automatizado (axe / Lighthouse) + manual (teclado, leitor de tela).

**CD → HML (homologação)**
- ambiente de staging, testes de integração/e2e em hml, *secrets de hml*.

## Definição de pronto

- [ ] estratégia de testes definida (pirâmide)
- [ ] ferramentas de qualidade configuradas (lint + type-check + coverage)
- [ ] testes de acessibilidade definidos (auto + manual), rastreados ao RNF
- [ ] CD → HML configurado (se aplicável)
- [ ] critérios de "pronto" atingidos (testes passando)
- [ ] todo item com Origem rastreável (rigor)
- [ ] nenhum item sem suporte na auditoria (rigor)
- [ ] usuário validou item a item (rigor)
