from typing import List
from http import HTTPStatus
from fastapi import APIRouter

from src.services import TrendsService
from src.services.schemas import BestAssetResponse


router = APIRouter()


@router.get(
    "",
    status_code=HTTPStatus.OK,
    response_model=List[BestAssetResponse],
    description="lists the best selling assets in the last few days",
)
async def list_best_assets(interval: int = 7, limit: int = 5):
    return TrendsService().filter_best_assets_by_last_days(interval, limit)
