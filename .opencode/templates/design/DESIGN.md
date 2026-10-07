---
version: alpha
name: <projeto>
description: <1 frase — a linguagem visual do projeto>

# Papéis semânticos (não só hex). Referencie com {colors.x} nos componentes.
colors:
  background: "#ffffff"
  surface: "#fafafa"
  text: "#171717"
  text-muted: "#4d4d4d"
  primary: "#171717"
  on-primary: "#ffffff"
  border: "#ebebeb"
  link: "#0070f3"
  success: "#1a7f37"
  warning: "#b45309"
  error: "#d1242f"

typography:
  display:
    fontFamily: <ex.: Inter, system-ui, sans-serif>
    fontSize: 32px
    fontWeight: 600
    lineHeight: 40px
    letterSpacing: -1.28px
  body:
    fontFamily: <ex.: Inter, system-ui, sans-serif>
    fontSize: 16px
    fontWeight: 400
    lineHeight: 24px
  caption:
    fontFamily: <...>
    fontSize: 12px
    fontWeight: 400
    lineHeight: 16px

rounded:
  sm: 6px
  md: 8px
  lg: 12px
  full: 9999px

spacing:
  xxs: 4px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 32px
  2xl: 48px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.md}"
  input:
    backgroundColor: "{colors.background}"
    textColor: "{colors.text}"
    borderColor: "{colors.border}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
---

# DESIGN — <projeto>

> Sistema visual do projeto. O `AGENTS.md` diz *como construir*; este diz *como
> deve parecer*. O agente lê este arquivo antes de construir/alterar UI.

## Overview
<A atmosfera visual em 1-2 parágrafos + 3-5 características-chave>

## Colors
- **background / surface / text / primary**: os papéis base.
- **Semânticas**: success / warning / error.
- Regra: **nunca hex cru nos componentes** — sempre `{colors.<papel>}`.

## Typography
| Token | Size | Weight | Line height | Uso |
|-------|------|--------|-------------|-----|
| `{typography.display}` | 32px | 600 | 40px | títulos |
| `{typography.body}` | 16px | 400 | 24px | corpo |
| `{typography.caption}` | 12px | 400 | 16px | rótulos |

## Layout
- **Espaçamento**: base 4px; tokens `{spacing.*}`.
- **Container/grid**: <largura máx, colunas>.
- **Responsivo**: breakpoints + alvos de toque (≥ 44×44px).

## Elevation & Depth
<tabela de níveis de sombra>

## Shapes
<raio de borda por uso>

## Components
Cada componente com **estados** (default / hover / focus / pressed / disabled) e
suas propriedades (`backgroundColor`, `textColor`, `rounded`, `padding`...).

## Do's and Don'ts
### Do
- ...
### Don't
- ...

## Acessibilidade
- Contraste ≥ 4.5:1 no texto; foco visível; rótulos/`aria`; navegação por teclado.

## Rastreia
- Decisões: [[...]]
- Fase: [[engenharia-software/04-design-de-modulos]]
