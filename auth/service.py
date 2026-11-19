from typing import Dict, Optional
from auth.crypto import hash_password, verify_password, create_jwt_token, verify_jwt_token

class AuthService:
    def __init__(self):
        self.users: Dict[str, dict] = {}

    def register(self, username: str, password: str) -> bool:
        if username in self.users:
            return False
        self.users[username] = {
            "username": username,
            "password_hash": hash_password(password)
        }
        return True

    def authenticate(self, username: str, password: str) -> Optional[str]:
        user = self.users.get(username)
        if not user or not verify_password(password, user["password_hash"]):
            return None
        return create_jwt_token({"sub": username})
