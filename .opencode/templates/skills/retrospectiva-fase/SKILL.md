---
name: retrospectiva-fase
description: Use when an engineering phase closes (the phase doc becomes `validado`) to produce a learning retrospective — a synthesis of what the student learned in that phase, not just the project. Saves to doc/vault/historico/retrospectivas/fase-N.md. Trigger keywords: fechar fase, retrospectiva, síntese de aprendizado, fase concluída.
---

# Retrospectiva por fase — síntese do aprendizado

Quando uma fase do processo de engenharia fecha (o doc da fase vira
`status: validado`), produza uma **retrospectiva de aprendizado** — sobre o
**aluno**, não sobre o projeto.

## Passos

1. **Reunir** as observações e avaliações do período da fase (em
   `doc/vault/historico/`) e o `estado-atual.md`.
2. **Preencher** o template `retrospectiva.md` (em
   `.opencode/templates/progressao/`):
   - conceitos trabalhados (nível início → fim, com evidência);
   - o que foi aprendido;
   - dificuldades / erros recorrentes;
   - lacunas remanescentes;
   - relação com o projeto (link pra fase).
3. **Salvar** em `doc/vault/historico/retrospectivas/fase-N.md`.
4. **Regenerar o índice** (script `gerar-index.ps1`).
5. **Confirmar** com um resumo de 1 linha.

## Regras

- É sobre o **aprendizado**, não sobre o projeto (isso fica no doc da fase).
- Toda afirmação cita **evidência** (rigor).
- Pergunte ao aluno as percepções; não invente.
