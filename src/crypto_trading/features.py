"""Feature computation for multi-factor strategies (synthetic / public data)."""

from typing import List, Dict, Any
import statistics

def compute_features(prices: List[float], volumes: List[float] = None) -> Dict[str, Any]:
    """Compute basic trend, momentum, volatility, and regime features."""
    if not prices or len(prices) < 2:
        return {"trend_strength": 0.0, "regime": "unknown", "anomaly_score": 0.0}

    returns = [(prices[i] - prices[i-1]) / prices[i-1] for i in range(1, len(prices))]
    vol = statistics.stdev(returns) if len(returns) > 1 else 0.0
    trend = (prices[-1] - prices[0]) / prices[0] if prices[0] else 0.0
    trend_strength = min(1.0, abs(trend) / (vol + 1e-6))

    regime = "low_vol" if vol < 0.02 else "high_vol" if vol > 0.05 else "neutral"
    anomaly_score = 0.8 if abs(returns[-1]) > 3 * vol else 0.1

    return {
        "trend_strength": round(trend_strength, 3),
        "regime": regime,
        "anomaly_score": round(anomaly_score, 3),
        "volatility": round(vol, 4),
        "last_return": round(returns[-1], 4) if returns else 0.0,
    }
