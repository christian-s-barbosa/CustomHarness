---
tipo: projeto
projeto: personalrag
tipo-projeto: desenvolvimento
atualizado: 2026-10-06
---

# personalrag

## Propósito
Núcleo reutilizável de **RAG** (Retrieval-Augmented Generation) sobre bases de
conhecimento em Markdown. Separa o motor (biblioteca) do conteúdo/config de cada
projeto. Expõe o motor via CLI e servidor MCP.

## Stack
- Python >=3.10, setuptools.
- Deps: chromadb, sentence-transformers, openai, python-frontmatter,
  python-dotenv; extra `mcp`.

## Estado
- Motor estruturado em `src/personalrag` (config, chunking, store, retrieve,
  generate, rag, cli, mcp, models).
- Sem testes ainda.

## Decisões principais
- Separação motor (biblioteca) ↔ conteúdo/config (Settings).
- Módulos: chunking (por seção + breadcrumb), store (embeddings + Chroma),
  retrieve (+ rerank opcional), generate (LLM compatível com OpenAI).

## Links
- [[historico/personalrag/engenharia-software/00-perguntas-em-aberto]]
