# Esqueleto comum — fase

Molde fixo, comum às 8 fases. O que varia está no guia de cada fase, que define
as seções de `## Conteúdo` e os itens específicos da `## Definição de pronto`.

```
---
fase: N
titulo: <Nome da Fase>
data: YYYY-MM-DD
status: rascunho
formato: <formato escolhido, quando aplicável (Fases 3 e 5)>
---

# Fase N — <Nome da Fase>

> **Status:** rascunho | validado
> **Fase:** N de 8

## Kanban
| Card | Título | Status |
|------|--------|--------|

## Objetivo
<o que esta fase busca responder>

## Conteúdo
<seções específicas da fase — ver guia fase-0N-<nome>.md>

## Decisões e racional
| Decisão | Descartou | Motivo | Origem |
|---------|-----------|--------|--------|

## Perguntas em aberto
- ...

## Definição de pronto (fase concluída)
- [ ] <itens específicos da fase — ver guia da fase>
- [ ] todo item com Origem rastreável (rigor)
- [ ] nenhum item sem suporte na auditoria (rigor)
- [ ] usuário validou item a item (rigor)

## Próximos passos
<o que a fase seguinte precisa deste documento>

## Navegação
← Anterior: [[...]] · → Próxima: [[...]]
```

## Notas

- `status` só vira `validado` após o gate humano (rigor, camada 4).
- `formato` aparece nas fases que têm menu (Fase 3: `just-enough | adr | c4`;
  Fase 5: `por-feature | diario | por-sprint`).
- A seção `## Kanban` só é preenchida se o projeto tiver board no GitHub.
