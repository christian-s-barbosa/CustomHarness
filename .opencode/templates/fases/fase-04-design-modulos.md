# Fase 4 — Design de módulos

**Objetivo:** detalhar a arquitetura (Fase 3) em módulos concretos — tipos,
responsabilidades e contratos — **ainda sem código**. É onde SOLID e design
patterns entram.

## Seções

**Módulos/pacotes**
| Módulo | Responsabilidade | Depende de | Status | Origem |

**Tipos principais**
| Tipo | Módulo | Campos/Atributos | Responsabilidade | Status | Origem |

**Interfaces/contratos**
| Contrato | Entre (módulos) | Assinatura | Comportamento esperado | Status | Origem |

**Limites e direção de dependência**
- o que cada módulo NÃO faz (fora do escopo dele);
- regra de dependência (ex.: camada interna não importa camada externa).

**Design da interface (UI)**
O sistema visual vive em `doc/vault/design/DESIGN.md` (molde em
`.opencode/templates/design/DESIGN.md`) — **fonte da verdade** do visual, seguida
ao construir/alterar UI. Para escolher estilo/paleta/tipografia, use o skill
**`ui-ux-pro-max`** (`.opencode/skills/ui-ux-pro-max/scripts/search.py
"<tipo de produto> <keywords>" --design-system`).

| Componente | Estados | Comportamento | Status | Origem |
|------------|---------|---------------|--------|--------|
- Acessibilidade: contraste, foco visível, semântica, ARIA.

**Diagrama (opcional)** — UML de classes/sequência em Mermaid.

**Rastreamento** — ligar cada módulo/contrato à Fase 3 (ADR) e aos RF da Fase 1.

## Definição de pronto

- [ ] cada módulo com responsabilidade e dependências definidas
- [ ] tipos principais com campos e responsabilidade
- [ ] contratos entre módulos definidos (assinatura + comportamento)
- [ ] limites e direção de dependência desenhados
- [ ] componentes de interface com estados definidos (se houver front-end)
- [ ] `doc/vault/design/DESIGN.md` preenchido (se houver front-end)
- [ ] rastreamento com Fase 3 (ADR) e RF preenchido
- [ ] todo item com Origem rastreável (rigor)
- [ ] nenhum item sem suporte na auditoria (rigor)
- [ ] usuário validou item a item (rigor)
