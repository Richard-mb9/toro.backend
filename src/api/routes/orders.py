from http import HTTPStatus
from fastapi import APIRouter, Depends

from src.commons.security import get_uid_from_token
from src.services import OrderService
from src.services.schemas import OrderRequest, CreateOrderResponse

router = APIRouter()


@router.post("", status_code=HTTPStatus.OK, response_model=CreateOrderResponse)
async def create(order: OrderRequest, user_id: int = Depends(get_uid_from_token)):
    return OrderService().create_order(user_id, order)
