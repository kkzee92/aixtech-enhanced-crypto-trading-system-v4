# Security Policy

## Supported Versions
- main branch (v4 and later)

## Reporting a Vulnerability
Please open a private security advisory or contact the maintainer. Do not disclose publicly until addressed.

## Design Principles
- Zero Trust: verify explicitly, least privilege, assume breach.
- No private keys, seeds, or exchange secrets in the repository or agent context.
- Synthetic fixtures only.
- Multi-layer redaction and audit seals.
- CI includes secret scanning and policy guards.

See docs/security-architecture.md for details.
