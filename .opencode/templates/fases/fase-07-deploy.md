# Fase 7 — Implementação / Deploy

**Objetivo:** colocar o resultado em produção — hospedagem, **CD → PROD**,
variáveis de ambiente e secrets, release e operação.

## Seções

**Ambiente de produção**
- hospedagem (VPS/cloud), topologia real — materializa a decisão de topologia da Fase 3.

**CD → PROD**
- pipeline de release: do HML validado (Fase 6) → prod; deploy com gate; **rollback**.

**Secrets e variáveis de ambiente**
| Secret/env | Onde vive | Como é gerido | Status | Origem |
> Regra dura: nunca versionado, via env vars / secrets manager (rastreia o RNF de Segurança).

**Release**
- versionamento (semver), tags, changelog, procedimento de rollback.

**Monitoramento / operação**
- logs, métricas, alertas, health check, backup (rastreia os RNF de Disponibilidade/Durabilidade).

## Definição de pronto

- [ ] produção no ar, topologia da Fase 3 materializada
- [ ] CD → PROD funcionando (release + rollback testado)
- [ ] secrets/env vars geridos fora do código (nada versionado)
- [ ] monitoramento + alertas + backup configurados
- [ ] todo item com Origem rastreável (rigor)
- [ ] nenhum item sem suporte na auditoria (rigor)
- [ ] usuário validou item a item (rigor)
