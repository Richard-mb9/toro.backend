from datetime import datetime

from src.commons.errors import NotFoundError, UnprocessableEntity
from src.infra.repositories import OrderRepository
from src.domain import Order

from .schemas import OrderRequest
from .account_service import AccountService
from .asset_service import AssetService
from .users_assets_service import UsersAssetsService


class OrderService:
    """Service for use Orders"""

    def __init__(self) -> None:
        self.repository = OrderRepository()

    def create_order(self, user_id, order: OrderRequest):
        account = AccountService().find_by_user_id(user_id)
        asset = AssetService().find_by_code(order.symbol)

        if asset is None:
            raise NotFoundError("Asset not Found")

        total_amount = asset.price * order.amount
        if account.amount < total_amount:
            raise UnprocessableEntity("insufficient funds")

        new_account_amount = float(account.amount) - float(total_amount)

        UsersAssetsService().put_item(user_id, order.symbol, order.amount)
        AccountService().update(account.id, new_account_amount)

        order = Order(
            user_id=user_id,
            asset_code=asset.code,
            quantity=order.amount,
            unity_value=asset.price,
            total_amount=total_amount,
            created_at=datetime.now(),
        )

        self.repository.insert(order)

    def filter_by_last_days(self, interval: int, limit: int):
        return self.repository.filter_by_last_days(interval, limit)
