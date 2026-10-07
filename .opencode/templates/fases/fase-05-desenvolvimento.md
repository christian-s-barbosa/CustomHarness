# Fase 5 — Desenvolvimento

**Objetivo:** implementar seguindo o design (Fase 4), respeitando convenções.
Cada feature usa o *Fluxo por Feature* (entender → desenhar → implementar →
verificar → revisar → documentar).

**Formato:** escolhido por contexto — `por-feature` (default, rastreabilidade),
`diario` (projeto pequeno, contexto/tempo), `por-sprint` (se houver kanban/sprints).

## Casco comum (os 3 formatos)

**Convenções**
| Convenção | Regra | Motivo | Status | Origem |

**CI / feedback do dev**
- build + lint + testes unitários automáticos a cada push.

## O miolo (varia por formato)

### `por-feature`
```
## Features implementadas
| Feature | RF rastreado | Módulos (Fase 4) | Status | Origem |

## Decisões de implementação
| Decisão | Desvia do design? | Motivo | Rastreia | Status | Origem |
```

### `diario`
```
## Diário (cronológico)
### YYYY-MM-DD — <tema>
- Feito: ...
- Decisões: ...
- Próximo: ...

## Features (resumo)
| Feature | RF | Estado | Origem |
```

### `por-sprint`
```
## Sprint N — <objetivo>
- Período: ...
- Cards/features: ...
- Entregue: ...
- Bloqueios/desvios: ...
```

## Definição de pronto

- [ ] convenções registradas e seguidas
- [ ] features implementadas conforme o design (ou desvio registrado com motivo)
- [ ] CI (build + lint + testes unitários) rodando
- [ ] rastreamento feature → RF → módulo preenchido
- [ ] todo item com Origem rastreável (rigor)
- [ ] nenhum item sem suporte na auditoria (rigor)
- [ ] usuário validou item a item (rigor)
