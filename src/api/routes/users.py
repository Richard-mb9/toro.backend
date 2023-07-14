from fastapi import APIRouter
from http import HTTPStatus

from src.services import UserService
from ...services.schemas import (
    CreateUserRequest,
    CreateUserResponse,
    UpdateUserRequest,
    UpdatePasswordRequest,
)

router = APIRouter()


@router.post("/", status_code=HTTPStatus.CREATED, response_model=CreateUserResponse)
async def create(user: CreateUserRequest):
    return UserService().create_user(user)


@router.put("/{userId}", status_code=HTTPStatus.OK, response_model=None)
async def update(userId: int, user: UpdateUserRequest):
    UserService().update_user(user_id=userId, data=user)


@router.put("/{userId}/password", status_code=HTTPStatus.OK, response_model=None)
async def update_password(userId: int, data: UpdatePasswordRequest):
    UserService().update_password(user_id=userId, data=data)
