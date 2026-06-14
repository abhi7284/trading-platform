from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext

from config.settings import settings
import bcrypt


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


class AuthService:

    @staticmethod
    def hash_password(password: str) -> str:
        return bcrypt.hashpw(
            password.encode(),
            bcrypt.gensalt()
        ).decode()

    @staticmethod
    def verify_password(
        password: str,
        hashed_password: str
    ) -> bool:
        return bcrypt.checkpw(
            password.encode(),
            hashed_password.encode()
        )

    @staticmethod
    def create_access_token(
        user_id: str
    ) -> str:

        payload = {
            "sub": user_id,
            "exp": datetime.utcnow() + timedelta(hours=24)
        }

        return jwt.encode(
            payload,
            settings.jwt_secret,
            algorithm=settings.jwt_algorithm
        )