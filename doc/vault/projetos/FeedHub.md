---
tipo: projeto
projeto: FeedHub
tipo-projeto: estudo
atualizado: 2026-10-06
---

# FeedHub

## Propósito
Site que agrega notícias (RSS), discussões (Reddit) e posts (Bluesky),
organizados por **temas**, com busca semântica (RAG) e leitura por TTS.

## Stack
- Back: Python/OOP (framework a definir).
- Front / banco / hospedagem: a definir.

## Estado
- Fases 01–08 documentadas no vault (requisitos, especificação, arquitetura,
  design, desenvolvimento, testes, deploy, manutenção).
- Ainda sem código.

## Decisões principais
- Frente social via Bluesky (AT Protocol) em vez de X/Threads.
- Organização por temas, com 3 seções (notícias / discussões / posts).
- Acesso: dono sempre + token temporário read-only.
- Hospedagem: Hetzner VPS (com possível migração pra self-host).

## Links
- [[historico/FeedHub/engenharia-software/01-levantamento-de-requisitos]]
