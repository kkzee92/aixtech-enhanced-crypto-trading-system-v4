"""Security utilities: enhanced redaction, multi-hash seals, anomaly stubs."""

import hashlib
import re
from typing import Dict

def redact_sensitive(text: str) -> str:
    """Redact potential private keys, seeds, high-entropy strings, API keys."""
    # Base58-like (private keys, addresses)
    text = re.sub(r'[1-9A-HJ-NP-Za-km-z]{40,}', '[REDACTED_KEY]', text)
    # Hex private keys
    text = re.sub(r'(0x)?[0-9a-fA-F]{64}', '[REDACTED_HEX]', text)
    # Simple seed phrase pattern (sequence of common words - stub)
    text = re.sub(r'\b(abandon|ability|able|about|above|absent|absorb|abstract|absurd|abuse)\b(?:\s+\w+){10,}', '[REDACTED_SEED]', text, flags=re.IGNORECASE)
    return text

def multi_hash_seal(data: str) -> Dict[str, str]:
    """Generate multi-hash seals for audit trails."""
    encoded = data.encode('utf-8')
    return {
        "sha256": hashlib.sha256(encoded).hexdigest(),
        "sha3_256": hashlib.sha3_256(encoded).hexdigest(),
        "blake2b": hashlib.blake2b(encoded).hexdigest(),
    }

def anomaly_score(log_entry: str) -> float:
    """Stub anomaly score based on length and simple entropy proxy."""
    if len(log_entry) > 1500:
        return 0.95
    # Rough entropy proxy: unique chars ratio
    unique_ratio = len(set(log_entry)) / max(1, len(log_entry))
    if unique_ratio > 0.7 and len(log_entry) > 200:
        return 0.75
    return 0.05
