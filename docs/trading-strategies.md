# Trading Strategies per Asset Class (v4 Enhanced)

All strategies produce **paper-only information signals**. Multi-factor adaptive rules with regime awareness, multi-timeframe confluence, and on-chain activity proxies. Assumptions documented; **not financial advice**.

## Common Building Blocks
- Trend: Adaptive EMA / Supertrend / ATR channels (multi-timeframe)
- Momentum: RSI, rate-of-change, MACD divergence
- Volatility: ATR percentile, regime clustering (low/med/high vol)
- Volume / Flow: relative volume, funding rate, open interest change
- Relative: strength vs benchmark (BTC/ETH), correlation filters
- On-chain / Activity proxies (synthetic where needed): TVL change, fee revenue, active addresses, developer activity
- Risk filters: anomaly score, drawdown, time-stop, correlation breakdown
- Adaptive parameters: selected based on recent volatility clustering and regime

## Asset Classes

| Class | Examples | Key Factors | Risk Profile | Notes |
|-------|----------|-------------|--------------|-------|
| Majors | BTC, ETH | Adaptive EMA + ATR + funding/OI + vol regime + MTF confluence | Medium | Core trend following with mean-reversion overlay in high vol |
| Large Alts | SOL, BNB, ADA | Relative strength + breakout + correlation to BTC + volume confirmation | Medium-High | Filter when BTC dominance rising sharply |
| DeFi | UNI, AAVE, LINK | Price + TVL/fee growth + isolation + risk-parity + protocol health | High | Protocol-specific risk gates, liquidity filters |
| Stables | USDT, USDC | Peg deviation + volume + netflow proxies | Low (alert only) | Alert on depeg > threshold; no directional trade |
| High Vol / Meme | DOGE, PEPE, new | Strict 0.5% risk, time stops, anomaly filter, volume burst | Very High | Tight stops, short holds, high anomaly gate |
| L2 | ARB, OP | Relative strength vs ETH + adaptive MTF + ecosystem narrative | Medium | Filter on L1 stress |
| RWA | Tokenized assets | Slow multi-scale + gap/anomaly halt + fundamental proxies | Low-Medium | Conservative, event-driven |
| Perpetuals | Perp markets | Funding carry + contained drift + OI change + basis | Medium | Funding arbitrage signals |
| AI-tokens | FET, AGIX, etc. | Hybrid burst + activity proxy + divergence + narrative strength | High | Narrative + technical confluence |
| GameFi | AXS, SAND, etc. | Activity + price relative + volume + seasonal filters | High | Event / season aware |
| Emerging | Restaking, modular | Activity growth + correlation + anomaly | High | Extra caution, smaller size |

Detailed rule stubs and enhancements in `src/crypto_trading/strategies.py`.

Enhancements in v4: improved regime detection via volatility clustering, multi-timeframe confluence scoring, expanded on-chain proxies, adaptive parameter selection, and clearer confidence calibration.
