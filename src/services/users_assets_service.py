from src.infra.repositories import UsersAssetsRepository
from src.domain import UsersAssets


class UsersAssetsService:
    """Service for users Assets"""

    def __init__(self):
        self.repository = UsersAssetsRepository()

    def put_item(self, user_id: int, asset_code: str, quantity: int):
        users_assets = self.repository.find_by_user_id_and_asset_code(
            user_id, asset_code
        )

        if users_assets is None:
            return self.__create(
                user_id=user_id, asset_code=asset_code, quantity=quantity
            )

        self.repository.update_quantity(
            user_id=user_id, asset_code=asset_code, quantity=quantity
        )

    def __create(self, user_id: int, asset_code: str, quantity: int):
        users_assets = UsersAssets(
            user_id=user_id, asset_code=asset_code, quantity=quantity
        )

        self.repository.insert(users_assets)
