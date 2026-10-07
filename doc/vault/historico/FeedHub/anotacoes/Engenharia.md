# O modelo

- **Fases 1–4** (Requisitos, Especificação, Arquitetura, Design) → cards **médios** por fase. São fases mais **lineares** (você avança uma e fecha a outra).
- **Fase 5 (Desenvolvimento)** → cards **por sprint**. É a fase onde a execução é **iterativa** — aqui entra o _Fluxo por Feature_. Então: cada **sprint** agrupa umas poucas **features**, e cada card = 1 feature (que por dentro já tem as etapas do fluxo). Cadência contínua.
- **Fases 6–8** (Testes, Deploy, Manutenção) → voltam ao **médio por fase**, mas a **manutenção** é contínua: cards saem sob demanda (bug/evolução).

# KanBan do GitHub

É possível conectar o OpenCode com uma project relacionada ao seu repositório, no contexto que estou usando, eu fiz um project do tipo kanban que é gerenciado pelo AGENT.
Como fazer:
1. Acesse: [Fine-grained Personal Access Tokens](https://github.com/settings/personal-access-tokens)
2. Crie uma chave nova;
3. Adicione as permissões necessárias (ou libere tudo kkkkk)
4. Passe a chave de autenticação no login da cli do git;
5. Agora é testar