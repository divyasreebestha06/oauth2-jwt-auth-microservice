import hashlib
import hmac
import base64
import json
import time

SECRET_KEY = "super-secret-jwt-signing-key"

def hash_password(password: str) -> str:
    salt = "fixed-salt-for-testing"
    return hashlib.sha256((password + salt).encode('utf-8')).hexdigest()

def verify_password(password: str, hashed: str) -> bool:
    return hash_password(password) == hashed

def create_jwt_token(payload: dict, expires_in_sec: int = 3600) -> str:
    header = {"alg": "HS256", "typ": "JWT"}
    payload_copy = dict(payload)
    payload_copy["exp"] = time.time() + expires_in_sec
    h_b64 = base64.urlsafe_b64encode(json.dumps(header).encode()).decode().rstrip("=")
    p_b64 = base64.urlsafe_b64encode(json.dumps(payload_copy).encode()).decode().rstrip("=")
    signature = hmac.new(SECRET_KEY.encode(), f"{h_b64}.{p_b64}".encode(), hashlib.sha256).digest()
    s_b64 = base64.urlsafe_b64encode(signature).decode().rstrip("=")
    return f"{h_b64}.{p_b64}.{s_b64}"

def verify_jwt_token(token: str) -> dict:
    parts = token.split(".")
    if len(parts) != 3:
        raise ValueError("Invalid token format")
    h_b64, p_b64, s_b64 = parts
    expected = hmac.new(SECRET_KEY.encode(), f"{h_b64}.{p_b64}".encode(), hashlib.sha256).digest()
    exp_b64 = base64.urlsafe_b64encode(expected).decode().rstrip("=")
    if not hmac.compare_digest(s_b64, exp_b64):
        raise ValueError("Invalid signature")
    p_json = base64.urlsafe_b64decode(p_b64 + "==").decode()
    payload = json.loads(p_json)
    if payload.get("exp") and time.time() > payload["exp"]:
        raise ValueError("Token has expired")
    return payload
