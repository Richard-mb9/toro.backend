from hashlib import md5
from src.services.schemas import (
    CreateUserRequest,
    UpdateUserRequest,
    UpdatePasswordRequest,
)
from src.domain import User
from src.infra.repositories import UserRepository
from src.commons.errors import ConflictError, NotFoundError, UnauthorizedError
from .accounts_service import AccountsService


class UserService:
    """Class User Service"""

    def __init__(self) -> None:
        self.repository = UserRepository()

    def create_user(self, user: CreateUserRequest):
        new_user = User(
            name=user.name,
            password=self.encode_password(user.password),
            email=user.email,
            cpf=user.cpf,
        )

        self.__validate_duplicate_data(email=user.email, cpf=user.cpf)

        user_created = self.repository.insert(new_user)
        AccountsService().create_account(user_created.id)
        return {"id": user_created.id}

    def update_user(self, user_id: int, data: UpdateUserRequest):
        self.find_by_id(user_id)
        self.repository.update(user_id, data.__dict__)

    def update_password(self, user_id: int, data: UpdatePasswordRequest):
        user = self.find_by_id(user_id)
        password = self.encode_password(data.current_password)
        new_password = self.encode_password(data.new_password)
        if user.password != password:
            raise UnauthorizedError("incorrect password")
        self.repository.update(user_id, {"password": new_password})

    def find_by_email(self, email: str):
        return self.repository.find_by_email(email)

    def find_by_cpf(self, cpf: str):
        return self.repository.find_by_cpf(cpf)

    def find_by_id(self, user_id):
        user = self.repository.find_by_id(user_id)
        if user is None:
            raise NotFoundError("User does not exist")
        return user

    def __validate_duplicate_data(self, email: str = None, cpf: str = None):
        if self.find_by_email(email) is not None:
            raise ConflictError("this email is already being used")
        if self.find_by_cpf(cpf) is not None:
            raise ConflictError("this cpf is already being used")

    def encode_password(self, password: str):
        return md5(password.encode("utf-8")).hexdigest()
