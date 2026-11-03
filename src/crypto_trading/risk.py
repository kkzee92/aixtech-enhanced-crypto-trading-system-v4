"""Risk gates and position sizing for paper signals."""

from typing import Dict, Any

def apply_risk_gates(signal: Dict[str, Any], risk_metrics: Dict[str, Any]) -> Dict[str, Any]:
    """Apply volatility targeting, drawdown, and anomaly gates."""
    result = signal.copy()
    drawdown = risk_metrics.get("drawdown", 0.0)
    if drawdown > 0.15:
        result.update(action="flat", confidence=1.0, reason="drawdown kill-switch")
    elif signal.get("anomaly_score", 0) > 0.8:
        result.update(action="flat", confidence=0.95, reason="anomaly risk gate")
    # Vol targeting stub: reduce confidence in high vol
    if signal.get("regime") == "high_vol":
        result["confidence"] = max(0.0, result.get("confidence", 0) * 0.6)
    return result
