from http import HTTPStatus
from fastapi import APIRouter

from ...services.schemas import AuthRequest, AuthResponse
from ...services import AuthService

router = APIRouter()


@router.post("/", status_code=HTTPStatus.OK, response_model=AuthResponse)
def auth(data: AuthRequest):
    return AuthService().login(data)
