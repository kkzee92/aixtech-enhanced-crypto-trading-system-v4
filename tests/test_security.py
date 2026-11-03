"""Tests for security utilities."""

from crypto_trading.security import redact_sensitive, multi_hash_seal, anomaly_score

def test_redact_key():
    text = "private key 5HueCGU8rMjxEXxiPuD5BDku4MkFqeZyd4dZ1jvhTVqvbTLvyTJ here"
    redacted = redact_sensitive(text)
    assert "[REDACTED_KEY]" in redacted
    assert "5Hue" not in redacted

def test_multi_hash_seal():
    seal = multi_hash_seal("test data")
    assert "sha256" in seal
    assert len(seal["sha256"]) == 64

def test_anomaly_score():
    assert anomaly_score("short") < 0.5
    assert anomaly_score("a" * 2000) > 0.8
