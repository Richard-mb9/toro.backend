from typing import List
from http import HTTPStatus
from fastapi import APIRouter


from src.services.schemas import AssetResponse
from src.services import AssetService

router = APIRouter()


@router.get(
    "",
    status_code=HTTPStatus.OK,
    response_model=List[AssetResponse],
    description="lists the best selling assets in the last few days",
)
async def list_assets():
    return AssetService().list_all()
