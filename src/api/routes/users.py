from http import HTTPStatus
from fastapi import APIRouter, Depends


from src.commons.security import verify_token, get_uid_from_token
from src.services import UserService
from ...services.schemas import (
    CreateUserRequest,
    CreateUserResponse,
    UpdateUserRequest,
    UpdatePasswordRequest,
    GetUserPositionResponse,
    GetAccountDataResponse,
)

router = APIRouter()


@router.post("", status_code=HTTPStatus.CREATED, response_model=CreateUserResponse)
async def create(user: CreateUserRequest):
    return UserService().create_user(user)


@router.put(
    "",
    status_code=HTTPStatus.OK,
    response_model=None,
    dependencies=[Depends(verify_token)],
)
async def update(user: UpdateUserRequest, user_id: int = Depends(get_uid_from_token)):
    UserService().update_user(user_id=user_id, data=user)


@router.put("/password", status_code=HTTPStatus.OK, response_model=None)
async def update_password(
    data: UpdatePasswordRequest, user_id: int = Depends(get_uid_from_token)
):
    UserService().update_password(user_id=user_id, data=data)


@router.get(
    "/account", status_code=HTTPStatus.OK, response_model=GetAccountDataResponse
)
async def get_account_data(user_id: int = Depends(get_uid_from_token)):
    return UserService().get_account_by_user_id(user_id=user_id)


@router.get(
    "/position", status_code=HTTPStatus.OK, response_model=GetUserPositionResponse
)
async def get_user_position(user_id: int = Depends(get_uid_from_token)):
    return UserService().get_user_position(user_id=user_id)
