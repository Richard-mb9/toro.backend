from src.domain import UsersAssets
from .base_repository import BaseRepository


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
