"""Offline demo of enhanced strategies and security checks for v4."""

from .features import compute_features
from .strategies import evaluate_strategy
from .risk import apply_risk_gates
from .security import multi_hash_seal, redact_sensitive

def run_demo():
    print("=== AIxTech Enhanced Crypto Trading System v4 (paper-only) ===")
    print("Running synthetic multi-asset strategy evaluation with enhanced factors...\n")

    # Synthetic price series for majors
    btc_prices = [60000, 60500, 61200, 60800, 62000, 63500, 62800]
    features = compute_features(btc_prices)
    signal = evaluate_strategy("majors", features)
    risked = apply_risk_gates(signal, {"drawdown": 0.04})
    print(f"Majors (BTC proxy): {risked}")

    # High vol / meme example
    meme_features = {"trend_strength": 0.25, "regime": "high_vol", "anomaly_score": 0.85}
    meme_signal = evaluate_strategy("high_vol", meme_features)
    print(f"High-Vol: {meme_signal}")

    # DeFi example
    defi_features = {"trend_strength": 0.65, "regime": "neutral", "anomaly_score": 0.2}
    defi_signal = evaluate_strategy("defi", defi_features)
    print(f"DeFi: {defi_signal}")

    # Security demo
    sample_log = "Signal generated for asset class majors. No secrets here."
    seal = multi_hash_seal(sample_log)
    print(f"\nAudit seal (multi-hash): SHA256={seal['sha256'][:16]}...")
    print(f"Redaction example: {redact_sensitive('key 5HueCGU8rMjxEXxiPuD5BDku4MkFqeZyd4dZ1jvhTVqvbTLvyTJ')}")

    print("\nAsset classes supported: Majors, Large Alts, DeFi, Stables, High-Vol, L2, RWA, Perpetuals, AI-tokens, GameFi, Emerging")
    print("Signals are paper-only. No orders placed. Security controls (redaction, seals, anomaly gates) applied.")
    print("Demo complete. See docs/ for full strategy and architecture details.")
    print("Research / educational use only. Not financial advice.")
