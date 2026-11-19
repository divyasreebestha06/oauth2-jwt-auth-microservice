# 🔒 oauth2-jwt-auth-microservice

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Security](https://img.shields.io/badge/Security-OAuth2_JWT-red?style=for-the-badge)](auth/)

Secure OAuth2 & JWT Authentication Microservice with bcrypt password hashing and token rotation.

## Security Highlights
- **Cryptographic Signatures:** Standard HMAC-SHA256 signature verification.
- **Expiry Enforcement:** Constant-time signature comparison and TTL checks.
- **Salted Hashing:** Mitigates rainbow table attacks against stored credentials.
