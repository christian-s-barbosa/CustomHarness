# Molde das fases — visão geral

Fonte canônica do processo de engenharia de software usado nos projetos (fases
1–8). Trabalha-se com **dois artefatos**:

- `esqueleto-fase.md` — o casco fixo (comum às 8 fases).
- `fase-0N-<nome>.md` — o guia de cada fase (o que preencher + a definição de pronto).

## As 8 fases

1. Levantamento de Requisitos
2. Especificação
3. Arquitetura
4. Design de módulos
5. Desenvolvimento
6. Testes de Qualidade
7. Implementação / Deploy
8. Manutenção (contínua)

## Protocolo de rigor (4 camadas — vale para todas as fases)

1. **Contrato de escrita** — toda tabela de itens tem colunas `Status`
   (`Confirmado` | `Hipótese` | `A confirmar`) e `Origem`, que é um **link**
   (`[[nota#ancora]]`) para a nota de onde o item veio — nunca texto livre.
   Célula vazia = "não levantado", nunca preenchida por suposição.
2. **Paráfrase é risco** — converter fala livre → item estruturado só vira
   `Confirmado` após o usuário confirmar a paráfrase. Sem confirmação =
   `Hipótese`/`A confirmar`.
3. **Auditoria de rastreabilidade** — antes de marcar `validado`, o agente roda
   um passe item a item: "de onde veio isso? o link aponta pra quê? o status
   está certo?". Item sem `Origem` (link) vira `Hipótese` ou `PQ`, nunca
   `Confirmado`.
4. **Gate humano** — readback item a item (`sim`/`não`/`corrige`); só então
   `status: validado`.

Gates presentes em toda "Definição de pronto":
- [ ] todo item com `Origem` (link) apontando pra fonte
- [ ] nenhum item sem suporte na auditoria
- [ ] usuário validou item a item

## Regras globais

- **Fases 1 e 2 são agnósticas de tecnologia.** Proibido definir linguagem,
  framework, banco, biblioteca, hospedagem ou ferramenta. Tecnologia que
  aparecer entra como **Restrição/Premissa** (se externa) ou **PQ** (se ideia),
  nunca como decisão. Stack é assunto da Fase 3.
- **UX/UI transversal:** UX (fluxos/wireframes) na Fase 2; UI (componentes,
  design system) na Fase 4.
- **Acessibilidade = categoria própria de RNF** e flui pelas fases:
  Fase 1 (RNF) → Fase 2 (critérios) → Fase 4 (design) → Fase 6 (testes).
- **Infra distribuída:**
  - Fase 3: topologia (onde roda) + estratégia de ambientes (dev/hml/prod).
  - Fase 5: CI (build + lint + testes unitários).
  - Fase 6: CD → HML (homologação, integração/e2e, secrets de hml).
  - Fase 7: CD → PROD (release, secrets de prod, monitoramento).

## Categorias de RNF

`Desempenho · Segurança · Disponibilidade · Usabilidade · Acessibilidade · Custo · Durabilidade`
