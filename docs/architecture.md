# Architecture (v4)

## High-level data flow
```mermaid
flowchart LR
    subgraph Inputs
        Pub["Public market data<br/>or synthetic fixtures"]
        OnChain["On-chain proxies<br/>(TVL, fees, activity - synthetic)"]
    end
    Pub --> Ingest["Ingestion + validation<br/>+ redaction"]
    OnChain --> Ingest
    Ingest --> Features["features.py<br/>trend, momentum, vol, regime,
multi-timeframe, correlation"]
    Features --> Strategies["strategies.py<br/>asset-class multi-factor<br/>adaptive rules"]
    Strategies --> Risk["risk.py<br/>vol-target, anomaly,
drawdown, correlation gates"]
    Risk --> Output["Paper signals + audit seal"]
    Output --> Demo["demo / CLI"]
```

## Process harness
Inspired by zeekiankok92:
- Task briefs with acceptance criteria
- AGENTS.md rules
- CI gates (lint, tests, secret scan, license)
- Human review + disclosure log
- Definition of Done = CI green + human sign-off

## Design choices
- Stdlib-preferring core for small attack surface.
- Injectable I/O for offline tests.
- Deterministic strategy stubs that are easily extended.
- Explicit paper-only constraint enforced in code comments and runtime checks.
