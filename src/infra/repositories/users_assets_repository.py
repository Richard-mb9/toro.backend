from typing import TypedDict, List
from sqlalchemy.sql import text
from src.domain import UsersAssets
from .base_repository import BaseRepository


class AssetsFromUser(TypedDict):
    """type result the assets from users"""

    asset_code: str
    quantity: int
    current_price: int


class UsersAssetsRepository(BaseRepository):
    """Repository from Users Assets"""

    def __init__(self):
        super().__init__(UsersAssets)

    def find_by_user_id_and_asset_code(
        self, user_id: int, asset_code: str
    ) -> UsersAssets | None:
        return (
            self.session.query(self.entity)
            .filter_by(user_id=user_id, asset_code=asset_code)
            .first()
        )

    def update_quantity(self, user_id: int, asset_code: str, quantity: int):
        asset = self.find_by_user_id_and_asset_code(user_id, asset_code)
        asset.quantity = quantity
        self.session.commit()
        return asset

    def list_by_user_id(self, user_id: int) -> List[AssetsFromUser]:
        query = (
            "select assets.code, users_assets.quantity, assets.price as current_price "
            "from users_assets "
            "inner join assets on assets.code = users_assets.asset_code "
            f"where users_assets.user_id = {user_id}"
        )

        result = self.session.execute((text(query)))

        return super().format_search_query(result)
