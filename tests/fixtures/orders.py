from datetime import datetime
from typing import List
from pytest import fixture
from src.domain import User, Asset, Order, UsersAssets
from src.infra.repositories import OrderRepository, UsersAssetsRepository
from src.infra.configs import DBConnectionHandler


def get_data_in_db(entity):
    session = DBConnectionHandler().get_session()
    return session.query(entity).filter().all()


def create_order(user_id: int, asset: Asset, quantity: int):
    total_amount = asset.price * quantity

    return Order(
        user_id=user_id,
        asset_code=asset.code,
        quantity=quantity,
        unity_value=asset.price,
        total_amount=total_amount,
        created_at=datetime.now(),
    )


def create_user_assets(user_id: int, asset: Asset, quantity: int):
    return UsersAssets(user_id=user_id, asset_code=asset.code, quantity=quantity)


@fixture
def orders(users, assets, clear_all_tables):
    users_in_db: List[User] = get_data_in_db(User)
    assets_in_db: List[Asset] = get_data_in_db(Asset)

    user_id = users_in_db[0].id
    asset_1 = assets_in_db[0]
    asset_2 = assets_in_db[1]

    order_1 = create_order(user_id, asset_1, 3)
    user_asset_1 = create_user_assets(user_id, asset_1, 3)
    order_2 = create_order(user_id, asset_2, 5)
    user_asset_2 = create_user_assets(user_id, asset_2, 5)

    repository = OrderRepository()
    user_assets_repository = UsersAssetsRepository()
    repository.insert(order_1)
    user_assets_repository.insert(user_asset_1)
    repository.insert(order_2)
    user_assets_repository.insert(user_asset_2)
