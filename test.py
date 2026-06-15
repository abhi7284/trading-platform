from jose import jwt

from config.settings import settings
from services.auth_service import AuthService

token = AuthService.create_access_token("user-123")

print("token:", token)

payload = jwt.decode(token, settings.jwt_secret, algorithms=[settings.jwt_algorithm])

print(payload)
