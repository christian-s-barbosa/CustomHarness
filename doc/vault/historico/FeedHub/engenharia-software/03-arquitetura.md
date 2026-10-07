---
fase: 3
titulo: Arquitetura
data: 2026-09-02
status: rascunho
milestone: Fase 3 — Arquitetura (#4)
---

# Fase 3 — Arquitetura

> **Status:** rascunho | validado
> **Fase:** 3 de 8

## Kanban

| Card | Título                                        | Status      |
| ---- | --------------------------------------------- | ----------- |
| #21  | Fase 3: Definir stack do backend              | Done        |
| #22  | Fase 3: Definir stack do frontend             | Done        |
| #23  | Fase 3: Definir banco de dados                | Done        |
| #24  | Fase 3: Definir infraestrutura                | Done        |
| #25  | Fase 3: Definir camadas e fluxos              | Todo        |
| #28  | ↳ Fluxo do worker (ingestão)                  | Todo        |
| #29  | ↳ Fluxo do site (exibição)                    | Todo        |
| #26  | Fase 3: Modelagem de dados e contratos de API | Todo        |
| #27  | Fase 3: Validar doc de arquitetura            | Todo        |
| #20  | Fase 3 — Arquitetura (épico)                  | In Progress |

> Prazo dos cards: 2026-09-04. As referências de card preenchem quando o card atinge `Done`.

## Objetivo

Decisões técnicas de alto nível: stack, camadas (dados/serviço/apresentação), como RSS e busca se conectam, modelagem de dados e contratos de API. Cada decisão registra o **porquê**.

## O que já está definido

<Em construção — definir stack, camadas, fluxos, dados e API.>

## Decisões e racional

| Decisão | Descartou | Motivo |
|---------|-----------|--------|
| Topologia: **App + Worker separados** (web e worker independentes) | Monólito único / serverless | Base de conhecimento vasta (muitas fontes); os jobs de fetch não podem travar o site |
| Agendamento: **`APScheduler`/beat** (decide *quando*) **+ RabbitMQ** (processa via fila, com `ack`/redelivery) | Só agendador embutido, sem fila | Separa o "quando" do "como processa sem perder/travar"; RabbitMQ (o usuário domina) garante robustez de entrega |
| Estado/integridade: **tabela de scheduler** no banco (last run, status) + **heartbeat do worker** | Contar só com o broker | Permite auditar e **recuperar jobs atrasados** ("deveria ter rodado e não rodou") |
| **Idempotência** no processamento | — | Redelivery do RabbitMQ não gera duplicado (buscar fonte já existente = atualizar) |
| **Banco único: PostgreSQL** (colunas relacionais + `JSONB` pro documento + `pgvector` pro RAG) | MongoDB (documento em banco separado) | Domínio relacional (conteúdo→fonte→tema N:N); RAG (pgvector) ao lado do texto; custo/backup simples (um banco só); JSONB dá a flexibilidade de documento sem segundo banco |
| **Imagem Postgres:** `pgvector/pgvector:pg16` (embute a extensão `pgvector`) | Imagem oficial `postgres` + instalar extensão à mão | A oficial não traz o `pgvector`; a `pgvector/pgvector` é mantida pelo autor da extensão e acompanha o Postgres — menos setup no deploy |
| **Hosting (PQ-04): Hetzner VPS** por enquanto, com **migração p/ servidor próprio (self-host) em casa** no futuro | PaaS (Fly/Render/Railway) e hospedagem compartilhada | Sempre online (sem cold start); roda web+worker+RabbitMQ+volume local; stack aberta (Docker) permite migrar "movendo a caixa" pro home-server |
| **Domínio + DNS: Hetzner** (registrar + DNS na mesma conta), com **migração p/ Cloudflare** no futuro (proxy/segurança) | Cloudflare desde já; registrar separado | Simples e coerente (VPS + Storage Box + domínio numa conta só); DNS sem proxy = certbot HTTP funciona direto (pré-req do RNF-10); migrar depois é só trocar nameservers — o proxy/DDoS do Cloudflare fica pra quando precisar |
| **Reverse proxy: nginx** (HTTPS via Let's Encrypt/certbot) | Caddy / Traefik | Mais usado/didático (skill transferível); serve áudio com Range; rate-limit (PQ-10); aprendizagem explícita de TLS |
| **Firewall/segurança da rede:** Hetzner Cloud Firewall + `ufw` no host — expõe só `80/443` (web via nginx) e `22` (SSH **somente chave** + fail2ban); **bloqueia** `5672/15672` (RabbitMQ) e `5432` (Postgres) à internet (só localhost) | Tudo exposto na internet | Minimiza superfície de ataque; só o nginx atende público; RabbitMQ/Postgres internos; SSH sem senha (chave) + fail2ban — RNF-02 |
| **Imagens:** baixar/armazenar as **imagens do corpo do artigo** (não só a capa), **redimensionadas (WebP)**, com o `src` reescrito para a versão local (image fetcher/rewriter) | Hotlink / só a capa | Imagens carregam informação (tabelas, gráficos, mensagens); hotlink quebra (bloqueio/CORS); uso pessoal |
| **Snapshot do feed:** XML cru **gzipado**, com **retenção limitada** (N dias, ex. 7), só para depurar/reprocessar | Guardar XML cru sem compressão/eternamente | XML comprime bem (gzip ~5–10x); retenção controla o custo de storage do VPS |
| **CI/CD: GitHub Actions** — push → lint/test → build Docker → push **GHCR** → VPS puxa e sobe (`docker compose up`); segredos no **Actions Secrets** | Deploy manual | Automatiza build/entrega; grátis no GitHub; testes/lint como gate (ferramentas definidas na Fase 6) |
| **Backend: Django** (server-rendered; admin + auth + ORM) — cadeia de deploy: `visitante → nginx (reverse proxy) → Gunicorn (WSGI) → Django` | FastAPI | Web é CRUD (o I/O pesado já está no worker); admin/auth aceleram login+cadastro (RF-05/07); deploy Django+nginx+Gunicorn é trilha batida; FastAPI fica para API pura/ML futura |
| **Frontend: monolito — Django templates + HTMX** (sem framework JS separado) | SPA em React/Vue/Next | Coerente com o Django (server-rendered); HTMX cobre interatividade (filtro por tema, player de áudio, painel); evita aprender um segundo framework JS agora |
| **Backup (RNF-11):** `pg_dump` agendado → **Hetzner Storage Box** (fora do VPS) | Backup no mesmo disco do VPS | Backup no mesmo host morre junto; offsite (Storage Box) garante durabilidade; cadência "periódica" alinhada ao RNF-11 |
| **Observabilidade/logs:** Docker log rotation (`json-file` + `max-size`) + logrotate no nginx; **uptime** via **Hetzner Cloud monitoring** (ping/servidor) + **UptimeRobot free** (HTTP/aplicação); **sem Sentry** | Sentry self-host; Uptime Kuma no mesmo VPS | Monitor **externo** grátis avisa mesmo se o VPS inteiro cair (interno morre junto); log rotation evita disco cheio; erro/status do worker já aparece no painel (RF-13); Sentry self-host precisa ~8GB+ e 20+ serviços, desproporcional ao projeto |
| **TTS: Piper** (self-hosted, grátis, leve em CPU) — gera áudio em **EN e pt-BR** | TTS cloud pago (OpenAI/ElevenLabs); Kokoro (qualidade maior, mas pt-BR fraco hoje) | Sem custo por uso (RNF-07); sem chave de API externa (RNF-08); roda leve no VPS (CPU); cobre EN + pt-BR, coerente com o conteúdo misto |

## Perguntas em aberto

Perguntas desta fase — detalhes em [[00-perguntas-em-aberto]]:
- [[00-perguntas-em-aberto|PQ-04]] Onde hospedar + HTTPS/secrets — *Resolvida (hosting) · HTTPS/secrets em andamento*

Lacunas de infra/DevOps identificadas na revisão (a debater):

- **Secrets em runtime (VPS)** — como os segredos chegam ao container rodando (ideia: variáveis de ambiente no servidor, sem `.env` no disco).
- **Volumes Docker** — persistência explícita de Postgres, RabbitMQ e mídia (áudio TTS + imagens WebP).
- **Renovação automática do certbot** — timer/cron + `restart: unless-stopped` nos containers.
- **Migrations no deploy** — entrypoint roda `migrate` antes de subir o web.

## Definição de pronto (fase concluída)

- [ ] Stack definida e justificada
- [ ] Camadas e fluxos desenhados
- [ ] Modelo de dados e contratos esboçados

## Próximos passos

Design de módulos (Fase 4): detalhar tipos, responsabilidades e interfaces.

## Navegação

← Anterior: [[02-especificacao|Fase 2 — Especificação]] | Próxima: [[04-design-de-modulos|Fase 4 — Design de Módulos]] →
