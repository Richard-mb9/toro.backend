from typing import List
from src.domain import Asset
from src.infra.repositories import AssetsRepository
from .schemas import AssetResponse


class AssetService:
    """Service for use Assets"""

    def __init__(self):
        self.repository = AssetsRepository()

    def find_by_code(self, code: str):
        return self.repository.find_by_code(code)

    def list_all(self) -> List[AssetResponse]:
        result: List[Asset] = self.repository.list()
        return [
            {"symbol": asset.code, "name": asset.name, "current_price": asset.price}
            for asset in result
        ]
