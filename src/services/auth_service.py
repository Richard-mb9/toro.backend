from datetime import datetime, timedelta
import jwt

from src.infra.repositories import UserRepository
from src.commons.errors import UnauthorizedError
from .schemas import AuthRequest
from .user_service import UserService
from src.config import SECRETKEY, EXP_TIME_MIN


class AuthSerivice:
    """Class for Services to authenticate"""

    def __init__(self):
        self.repository = UserRepository()
        self.user_service = UserService()

    def login(self, data: AuthRequest):
        user = self.user_service.find_by_email(data.email)
        if user is None:
            raise UnauthorizedError("Incorrect Credentials")

        password = self.user_service.encode_password(data.password)

        if user.password != password:
            raise UnauthorizedError("Incorrect Credentials")

        payload = {"uid": user.id}
        access_token = self.__generate_token(payload)
        return {"access_token": access_token, "token_type": "Bearer"}

    def __generate_token(self, payload: dict):
        return jwt.encode(
            {**payload, "exp": datetime.utcnow() + timedelta(minutes=EXP_TIME_MIN)},
            key=SECRETKEY,
            algorithm="HS256",
        )
