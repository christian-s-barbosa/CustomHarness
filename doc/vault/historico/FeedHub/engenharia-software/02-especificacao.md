---
fase: 2
titulo: Especificação
data: 2026-09-03
status: validado
milestone: Fase 2 — Especificação (#2)
---

# Fase 2 — Especificação

> **Status:** rascunho | validado
> **Fase:** 2 de 8

## Kanban

| Card | Título                                     | Status |
| ---- | ------------------------------------------ | ------ |
| #9   | Fase 2: Definir critérios de aceite dos RF | Done   |
| #10  | Fase 2: Definir medida dos RNF             | Done   |
| #11  | Fase 2: Validar doc de especificação       | Done   |
| #8   | Fase 2 — Especificação (épico)             | Done   |

> Prazo dos cards: 2026-09-02. As referências de card preenchem quando o card atinge `Done`.

## Objetivo

Transformar cada RF em **critérios de aceite mensuráveis** (formato Dado/Quando/Então) e cada RNF em uma **medida verificável**.

## O que já está definido

### RF-01 — Agregar notícias via RSS de fontes curadas

> **Propósito:** o FeedHub puxa as notícias das fontes RSS que você cura, para preencher a seção de notícias de cada tema.

Critérios de aceite (fonte já cadastrada; o foco é a **agregação** de artigos):

| ID    | Critério (Dado / Quando / Então)                                                                                                                                         |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| AC-01 | Dada uma fonte RSS **válida** cadastrada, **quando** o sistema agrega as fontes, **então** salva cada artigo com **título, link, data de publicação, autor e conteúdo**. |
| AC-02 | Dada uma fonte cadastrada, **quando** ela está fora do ar ou retorna erro, **então** o sistema **sinaliza a falha** e **continua processando as demais fontes**.         |

> Modelo: 1 caminho feliz + 1 caso de erro. Um AC por comportamento; variação de quantidade vai para os testes (fase 6).

### RF-02 — Buscar discussões do Reddit relacionadas aos temas

> **Propósito:** traz as discussões dos subreddits que você associa aos temas, com filtro por upvotes/recentes, para a seção de discussões.

Critérios de aceite (a fonte é um **subreddit** associado ao tema; o foco é a **busca e extração** de posts, com **filtro por upvotes (top) e recentes**):

| ID    | Critério (Dado / Quando / Então)                                                                                                                                                               |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AC-01 | Dado um tema com comunidades do Reddit associadas, **quando** busca pelas discussões mais recentes, **então** salva cada uma delas **vinculada ao tema**, com **título, link, data de publicação, autor e conteúdo**. |
| AC-02 | Dado um tema com comunidades associadas, **quando** a API do Reddit está fora do ar, **então** o sistema **sinaliza a falha** e registra o erro.                                                                         |
| AC-03 | Dado um tema com comunidades associadas, **quando** a API do Reddit **bloqueia o acesso temporariamente** (rate limit), **então** o sistema sinaliza a falha, espera e **tenta novamente** (retry).                 |

> Modelo: 1 caminho feliz + 2 casos de erro. Um AC por comportamento; variação de quantidade vai para os testes (fase 6).

### RF-03 — Listar postagens iniciais de perfis seguidos no Bluesky (sem respostas)

> **Propósito:** lista as postagens iniciais dos perfis que você acompanha (sem as respostas do fio), para a seção de posts.

Critérios de aceite (perfis já cadastrados; o foco é a **busca e extração** das postagens iniciais no Bluesky):

| ID    | Critério (Dado / Quando / Então)                                                                                                                                                       |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AC-01 | Dada uma lista de perfis seguidos, **quando** o sistema busca as postagens, **então** salva **a postagem inicial** de cada perfil (**sem as respostas** ao fio), com **link, data de publicação, autor e conteúdo**. |
| AC-02 | Dado uma lista de perfis, **quando** a API do Bluesky está fora do ar, **então** o sistema **sinaliza a falha** e registra o erro.                                                     |
| AC-03 | Dado uma lista de perfis, **quando** a API do Bluesky **bloqueia o acesso temporariamente** (rate limit), **então** o sistema sinaliza a falha, espera e **tenta novamente** (retry).  |

> Modelo: 1 caminho feliz + 2 casos de erro. Um AC por comportamento; variação de quantidade vai para os testes (fase 6).


### RF-04 — Organizar por temas; cada tema exibe as 3 seções filtradas (notícias / discussões / posts)

> **Propósito:** organiza tudo por tema: a página do tema mostra as 3 seções separadas, cada uma só com o seu tipo de conteúdo.

Critérios de aceite (o foco é a **organização e exibição** das seções):

| ID    | Critério (Dado / Quando / Então)                                                                                                                                                                                                              |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AC-01 | Dado um tema existente, **quando** o usuário acessa a página do tema, **então** as **3 seções são exibidas separadas**, cada uma **apenas com o seu tipo de conteúdo filtrado pelo tema** (notícias RSS / discussões Reddit / posts Bluesky). |
| AC-02 | Dado que o tema **não existe**, **quando** o usuário tenta acessá-lo, **então** o sistema **sinaliza que não há esse tema** (não encontrado).                                                                                                 |
| AC-03 | Dado um tema com uma seção **sem conteúdo**, **quando** o usuário acessa essa seção, **então** ela é exibida com **estado vazio** (sem erro).                                                                                                 |

> Modelo: 1 caminho feliz + 2 casos de erro. Um AC por comportamento; variação de quantidade vai para os testes (fase 6).

### RF-05 — Cadastrar tema e fonte individualmente, pela interface

> **Propósito:** você cadastra e edita temas e fontes (RSS/site, subreddit ou perfil) pela interface, associando cada fonte a um ou mais temas.

Critérios de aceite (o foco é no **cadastro** de tema e fonte):

| ID    | Critério (Dado / Quando / Então)                                                                                                    |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------- |
| AC-01 | Dado que o usuário acessa a interface de criação de tema, **quando** preenche o formulário corretamente, **então** o sistema cria o tema.                     |
| AC-02 | Dado que o usuário acessa a interface de criação de fonte, **quando** preenche o formulário corretamente, **então** o sistema cria a fonte e a **associa ao tema**.  |
| AC-03 | Dado que o usuário cadastra uma fonte, **quando** o link não é um feed válido (ou a fonte já existe), **então** o sistema **não cadastra** e mostra o erro. |
| AC-04 | Dado que o usuário cria um tema, **quando** o nome está vazio ou já existe, **então** o sistema **não cria** e mostra o erro. |

> Modelo: 2 caminho feliz + 2 casos de erro. Um AC por comportamento; variação de quantidade vai para os testes (fase 6).

### RF-06 — Cadastrar temas/fontes em massa via CSV

> **Propósito:** permite importar vários temas/fontes de uma vez por CSV, para não fazer um a um.

Critérios de aceite (o foco é no **cadastrar** do temas/fontes):

| ID    | Critério (Dado / Quando / Então)                                                                                                                                                                                                           |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| AC-01 | Dado que o dono envia um CSV com temas/fontes, **quando** todas as linhas estão com os tipos de dados corretos, **então** o sistema registra todos os temas/fontes e retorna um relatório de sucesso.                      |
| AC-02 | Dado que o dono do site enviou um csv com os temas/fontes, **quando** algumas linhas têm links inválidos, **então** o sistema registra as linhas válidas e retorna um relatório com os **sucessos e erros**. |
| AC-03 | Dado que o dono do site enviou um csv com os temas/fontes, **quando** o CSV está sem o cabeçalho, **então** o sistema rejeita a importação e notifica o usuário do erro.                                                                                         |



> Modelo: 1 caminho feliz + 2 casos de erro. Um AC por comportamento; variação de quantidade vai para os testes (fase 6).

### RF-07 — Login do dono (acesso + edição de temas/fontes)

> **Propósito:** protege o app — só você (dono) entra e edita; quem não está autenticado não acessa as áreas protegidas.

Critérios de aceite (o foco é no **login** do usuário):

| ID    | Critério (Dado / Quando / Então)                                                                                                                                                                                      |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AC-01 | Dado que o usuário é **dono**, **quando** ele digita as credenciais de administrador de forma correta, **então** o site o **autentica**, redireciona para a home **e habilita o acesso de edição** de temas e fontes. |
| AC-02 | Dado que o usuário **não está autenticado**, **quando** acessa uma rota protegida (página de edição), **então** o sistema **bloqueia o acesso** e/ou redireciona para o login.                                        |
| AC-03 | Dado que o usuário é **visitante** (com/sem token), **quando** ele tenta editar temas/fontes via API, **então** o sistema **nega a chamada (403)** e **registra a tentativa**.                                        |



> Modelo: 1 caminho feliz + 2 casos de erro. Um AC por comportamento; variação de quantidade vai para os testes (fase 6).

### RF-08 — Emitir token temporário read-only para visitantes

> **Propósito:** permite mostrar o site a visitantes por um período, só leitura, sem que eles possam editar.

Critérios de aceite (o foco é no **gerenciamento** do visitante):

| ID    | Critério (Dado / Quando / Então)                                                                                                                                             |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AC-01 | Dado que o dono quer emitir acesso, quando gera um token temporário, então cria um token com expiração e escopo read-only.                                                   |
| AC-02 | Dado que o usuário é **visitante**, **quando** recebe o token de acesso do dono, **então** ele consegue se logar.                                                            |
| AC-03 | Dado que o usuário é **visitante**, **quando** token expira, **então** ele será redirecionado à tela de login.                                                               |
| AC-04 | Dado que o usuário é **visitante**, **quando** ele tenta acessar explicitamente as APIs de escrita, **então** o sistema **nega a chamada (403)** e **registra a tentativa**. |

### RF-09 — Publicar o site em acesso público (dono sempre + visitantes via token)

> **Propósito:** publica o FeedHub na internet (não fica só na sua máquina); você (dono) entra e gerencia sempre; visitantes só entram com token e não editam.

Critérios de aceite (o foco é na **publicação e no acesso** ao site — conteúdo exige autenticação: dono ou token):

| ID    | Critério (Dado / Quando / Então)                                                                                                                                                                                          |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AC-01 | Dado o site publicado, **quando** qualquer pessoa acessa a URL pública, **então** o site responde e está no ar.                                                                                                                     |
| AC-02 | Dado o **dono** autenticado, **quando** acessa o site, **então** tem acesso pleno (ver **e** editar temas/fontes).                                                                            |
| AC-03 | Dado um **visitante** com **token válido**, **quando** acessa o site, **então** visualiza o conteúdo (**somente leitura**). |
| AC-04 | Dado que alguém acessa **sem** login e **sem** token, **quando** tenta ver o conteúdo, **então** é redirecionado ao login e o conteúdo **não** é exibido.                      |


> Modelo: 3 caminho feliz + 1 caso de erro. Um AC por comportamento; variação de quantidade vai para os testes (fase 6).

### RF-10 — Ouvir os textos como áudio: TTS gerado no backend + player próprio

> **Propósito:** permite ouvir qualquer texto (artigo, discussão ou post) como **áudio** gerado no backend (TTS), reproduzido num **player próprio** e servido **via streaming** (áudio gerado inteiro uma vez e cacheado — PQ-11).

Critérios de aceite (o foco é na **geração e reprodução** do áudio via streaming):

| ID    | Critério (Dado / Quando / Então)                                                                                                       |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------- |
| AC-01 | Dado o usuário em um **conteúdo** (artigo, discussão ou post), **quando** clica para escutar, **então** o áudio é **reproduzido via streaming** (começa a tocar sem baixar o arquivo todo). |
| AC-02 | Dado o usuário escutando, **quando** a conexão cai, **então** o sistema mostra uma mensagem de erro de conexão (sem quebrar a página).  |



| AC-03 | Dado que o usuário aciona "ouvir", **quando** a geração do TTS falha (texto muito longo ou erro no backend), **então** o sistema informa o erro e **não** reproduz o áudio. |

> Modelo: 1 caminho feliz + 2 casos de erro. Um AC por comportamento; variação de quantidade vai para os testes (fase 6).

### RF-13 — Painel de status do agendador/worker

> **Propósito:** dar visibilidade ao dono sobre o que o worker está fazendo — fontes processadas, última execução, erros e heartbeat — lendo a tabela de scheduler no Postgres (web e worker desacoplados, se falam pelo banco).

Critérios de aceite:

| ID    | Critério (Dado / Quando / Então) |
| ----- | -------------------------------- |
| AC-01 | Dado que o dono está logado, **quando** acessa o painel de status, **então** vê cada fonte com a **última execução** (sucesso/erro) e a data/hora. |
| AC-02 | Dado que um job de fetch falhou, **quando** o dono abre o painel, **então** vê o **erro registrado** daquela fonte. |
| AC-03 | Dado que o worker parou de responder (sem heartbeat), **quando** o dono abre o painel, **então** vê um **alerta** de worker inativo. |

### Medidas dos RNF (verificáveis)

| RNF | Medida (como verifico) |
|-----|------------------------|
| RNF-01 Frescura | fonte atualiza no intervalo padrão: Bluesky ≤ 1h; Reddit ≤ 24h; RSS manhã+noite (2x/dia). Verifico pelo timestamp da última atualização. |
| RNF-02 Segurança de acesso | toda rota protegida sem credencial → 401/redireciona; nenhum conteúdo acessível sem autenticação. |
| RNF-03 Responsiva | mobile-first: adapta de 320px até desktop, sem scroll horizontal; usável em 360×640. |
| RNF-04 Token (expiração + read-only) | token expira em ≤ N dias (N a definir — PQ-05); qualquer escrita com token → 403. |
| RNF-05 Disponibilidade | uptime ≥ 99% (meta); site responde na maioria das verificações (tensão com free tier — ver PQ-04). |
| RNF-07 Custo (free tier) | consumo (banda, requisições, storage) sempre abaixo do limite free; alerta ≥ 80%. |
| RNF-08 Segredos | nenhum token/chave em git/front/logs (varredura = 0); secrets só em variáveis de ambiente/secrets do hosting. |
| RNF-09 Desempenho | página/tema < 2s; busca/consulta < 1s. |
| RNF-10 HTTPS | toda requisição via HTTPS/TLS (certificado válido; nunca HTTP puro). |
| RNF-11 Durabilidade | backup/export da curadoria periódico (ex.: diário) e restauração testada. |

## Decisões e racional

| Decisão | Descartou | Motivo |
|---------|-----------|--------|
| Vínculo perfil Bluesky → tema por **palavras-chave** (MVP), evoluindo para **embeddings** (RAG) | Classifier ML treinado (não-LLM) | Regras determinísticas são baratas e explicáveis; embeddings reusam o vetorial/RF-11 sem dados rotulados; classifier exige rotulagem + treino + manutenção (alto custo p/ app pessoal) |
| Fonte Reddit = **subreddit** com filtro **upvotes (top) e recentes** | Busca por palavra-chave; subreddit sem filtro | Subreddit permite curar as melhores comunidades; filtro por relevância/recência |

## Perguntas em aberto

Perguntas desta fase — detalhes em [[00-perguntas-em-aberto]]:
- [[00-perguntas-em-aberto|PQ-06]] Fonte Reddit (subreddit vs busca) — *Resolvida*
- [[00-perguntas-em-aberto|PQ-07]] Perfil Bluesky → tema — *Resolvida*
- [[00-perguntas-em-aberto|PQ-08]] Interações no BlueSky (thread/fio) — *Aberta*
- [[00-perguntas-em-aberto|PQ-09]] Interface de Cadastro (Tema/Fonte) — *Aberta*
- [[00-perguntas-em-aberto|PQ-10]] Token: bloqueio por abuso — *Aberta*


## Definição de pronto (fase concluída)

- [x] Todos os RF com critérios de aceite (Dado/Quando/Então)
- [x] Todos os RNF com medida verificável

## Próximos passos

Arquitetura (Fase 3): transformar os requisitos em decisões de stack, camadas e modelagem.

## Navegação

← Anterior: [[01-levantamento-de-requisitos|Fase 1 — Levantamento de Requisitos]] | Próxima: [[03-arquitetura|Fase 3 — Arquitetura]] →
