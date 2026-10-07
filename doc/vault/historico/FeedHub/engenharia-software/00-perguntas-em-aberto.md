---
titulo: Perguntas em Aberto
tipo: indeces
status: em uso
---

# Perguntas em Aberto (decidir / documentos)

> Índice central das **decisões pendentes** do FeedHub. Cada fase/doc de engenharia referencia este arquivo em vez de duplicar as perguntas.
> `Resolvida` = já decidida (com a decisão registrada). `Aberta` = aguarda decisão (com o impacto e a fase/demanda).
> Conexões com o board: cada item aberto costuma ter relação com um card da fase.

## Abaixo — todas as pendências

### PQ-01 — Frequência de atualização das fontes
- **Status:** Resolvida
- **Impactos:** RNF-01
- **Decisão:** padrão por tipo de fonte — BlueSky a cada 1h, Reddit a cada 1 dia, RSS manhã e noite (campo configurável).

### PQ-02 — Vínculo tema ↔ fonte
- **Status:** Resolvida
- **Impactos:** RF-04, RF-05
- **Decisão:** N:N — uma fonte (RSS/site, subreddit ou perfil) pode pertencer a vários temas.

### PQ-03 — Esquema/validação do CSV
- **Status:** Aberta
- **Impactos:** RF-06 · Design (Fase 4)
- **Decisão:** — (aguarda; abrange colunas, formatos e como vincula linha a tema.)

### PQ-04 — Onde hospedar + HTTPS/secrets
- **Status:** Resolvida (hosting) · HTTPS/secrets em andamento (reverse proxy, Fase 3)
- **Impactos:** Fase 3 (Arquitetura) · Fase 7 (Deploy)
- **Decisão:** **Hetzner VPS** por enquanto (custo baixo, sempre online), com **migração para servidor próprio (self-host) em casa** no futuro. HTTPS/TLS e gestão de segredos ficam no tópico de reverse proxy/CI-CD.

### PQ-05 — Duração/UX do token
- **Status:** Aberta
- **Impactos:** RF-08 · Fase 2/3
- **Decisão:** — (aguarda — duração padrão e a UX de gerar o token.)

### PQ-06 — Fonte Reddit: subreddit ou busca por palavra-chave?
- **Status:** Resolvida
- **Impactos:** RF-02, RF-05
- **Decisão:** subreddit (comunidade curada), com **filtro por upvotes (top) e recentes**.

### PQ-07 — Como identificar o tema com um perfil do BlueSky?
- **Status:** Resolvida
- **Impactos:** RF-03, RF-05
- **Decisão:** vínculo por **palavras-chave** (MVP); evoluir para **embeddings/similaridade semântica** com o RAG (RF-11). Não treinar classifier no MVP.

### PQ-08 — Interações no BlueSky (threads/fio)
- **Status:** Aberta
- **Impactos:** RF-03
- **Decisão:** — (aguarda — por limitação de caracteres e uso de threads, avaliar recuperar o **fio (thread)** principal do post.)

### PQ-09 — Interface de Cadastro (Tema e Fonte juntas?)
- **Status:** Aberta
- **Impactos:** RF-05 · Design (Fase 4)
- **Decisão:** — (aguarda — decidir se as interfaces de Tema e Fonte são uma só ou separadas.)

### PQ-10 — Token: política de bloqueio por abuso
- **Status:** Aberta
- **Impactos:** RF-08
- **Decisão:** — (aguarda — bloqueio **automático via rate-limit** ou **manual** (dono revoga).)

### PQ-11 — Como servir o áudio do TTS (download vs streaming)
- **Status:** Resolvida
- **Impactos:** RF-10 · Fase 3/4 (Arquitetura/Design)
- **Decisão:** o backend **gera o áudio inteiro (TTS) uma vez** e **cacheia** (não regenera a cada play), e **serve via streaming** — o player consome em **segmentos / HTTP Range**, sem baixar o arquivo todo de uma vez e sem acoplar a geração (TTS) ao player. Padrão de streaming como Spotify/YouTube.
