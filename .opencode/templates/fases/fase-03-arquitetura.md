# Fase 3 — Arquitetura

**Objetivo:** decisões técnicas de alto nível — stack, camadas, topologia,
contratos — cada decisão com o porquê. **Aqui a tecnologia entra.**

**Formato:** escolhido no início da fase, por contexto. Opções:
- `just-enough` — projeto pequeno/protótipo, poucas decisões.
- `adr` — muitas decisões técnicas, foco no porquê (favorito p/ estudo).
- `c4` — vários componentes/integrações, precisa do mapa.

> Os formatos não são mutuamente exclusivos (ex.: `adr` + um diagrama C4).

## Seções comuns (os 3 formatos)

**Restrições (inputs das fases 1–2)**
| Restrição | Tipo | Origem (fase/PQ) | Impacto |

**Topologia / onde roda** (obrigatório, 1 nível)
- onde roda (VPS/cloud/serverless/on-prem), containers/processos, como se comunicam.

**Estratégia de ambientes**
- dev / hml / prod, e para que cada um serve.

## Formatos

### `just-enough`
```
## Stack
| Item | Escolha | Justificativa (1 linha) | Rastreia (PQ) | Status | Origem |

## Estrutura do projeto
<árvore de pastas/módulos>

## Decisões-chave (2–3)
- <decisão> — <1 linha do porquê>

## Riscos e pendências
```

### `adr`
```
## Visão geral
<1 parágrafo do sistema>

## Decisões de Arquitetura (ADRs)
### ADR-01 — <título>
- Contexto: <problema/restrição que motiva>
- Decisão: <o que foi escolhido>
- Descartou: <alternativas>
- Motivo: <por quê, com trade-offs>
- Rastreia: <← PQ-xx / restrição que resolve>

## Stack (resumo)
| Item | Escolha | Rastreia (ADR/PQ) | Status | Origem |

## Componentes (breve)
- <camadas/módulos principais>

## Riscos e pendências
```

### `c4`
```
## Nível 1 — Contexto do sistema
<quem usa + com o que conversa> + diagrama Mermaid

## Nível 2 — Containers
<peças maiores: web, api, banco, worker> + diagrama Mermaid

## Nível 3 — Componentes (opcional)

## Decisões-chave (ADR resumido)
- <decisão> — <porquê em 1–2 linhas>

## Stack
| Item | Escolha | Justificativa | Rastreia (PQ) | Status | Origem |

## Riscos e pendências
```

## Definição de pronto

- [ ] restrições das fases 1–2 listadas com origem
- [ ] topologia definida (onde roda)
- [ ] estratégia de ambientes (dev/hml/prod) definida
- [ ] PQs de tecnologia vindas das fases 1–2 resolvidas (ou explicitamente reabertas)
- [ ] formato escolhido preenchido (stack/ADR/diagramas conforme o caso)
- [ ] todo item com Origem rastreável (rigor)
- [ ] nenhum item sem suporte na auditoria (rigor)
- [ ] usuário validou item a item (rigor)
