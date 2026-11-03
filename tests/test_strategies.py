"""Tests for strategy evaluation."""

from crypto_trading.strategies import evaluate_strategy

def test_majors_long_signal():
    features = {"trend_strength": 0.7, "regime": "low_vol", "anomaly_score": 0.2}
    signal = evaluate_strategy("majors", features)
    assert signal["action"] == "long"
    assert signal["confidence"] > 0.5

def test_high_vol_anomaly_gate():
    features = {"trend_strength": 0.3, "regime": "high_vol", "anomaly_score": 0.9}
    signal = evaluate_strategy("high_vol", features)
    assert signal["action"] == "flat"
    assert signal["confidence"] == 1.0

def test_stables_alert():
    features = {"anomaly_score": 0.6, "regime": "neutral"}
    signal = evaluate_strategy("stables", features)
    assert signal["action"] == "alert"
