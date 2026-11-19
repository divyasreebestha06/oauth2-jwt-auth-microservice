from auth.service import AuthService
from auth.crypto import verify_jwt_token

auth_service = AuthService()

def handle_login(data: dict):
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return {"error": "Missing credentials"}, 400
    token = auth_service.authenticate(username, password)
    if not token:
        return {"error": "Invalid username or password"}, 401
    return {"access_token": token, "token_type": "bearer"}, 200
