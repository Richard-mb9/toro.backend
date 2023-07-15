from http import HTTPStatus
from fastapi import APIRouter

from ...services.schemas import AuthRequest, AuthResponse
from ...services import AuthSerivice

router = APIRouter()


@router.post("/", status_code=HTTPStatus.OK, response_model=AuthResponse)
def auth(data: AuthRequest):
    return AuthSerivice().login(data)
