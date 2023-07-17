from typing import List
from json import dumps
from http import HTTPStatus
from tests.fixtures.app import Client
from src.infra.configs import DBConnectionHandler
from src.domain import User, Asset
from src.services import AccountService


def get_data_in_db(entity):
    session = DBConnectionHandler().get_session()
    return session.query(entity).filter().all()


def transfer(client: Client, user_id: int, cpf: str, value: float):
    account = AccountService().find_by_user_id(user_id)

    payload = {
        "event": "TRANSFER",
        "target": {"bank": "352", "branch": "0001", "account": str(account.id)},
        "origin": {"bank": "033", "branch": "03312", "cpf": cpf},
        "amount": value,
    }

    response = client.post("/toro/spb/events", data=dumps(payload))
    return response


def test_should_create_order(client: Client, users, assets):
    users_in_db: List[User] = get_data_in_db(User)
    assets_in_db: List[Asset] = get_data_in_db(Asset)

    user_id = users_in_db[0].id
    asset_code = assets_in_db[0].code

    transfer(client, user_id, users_in_db[0].cpf, 1000)

    payload = {"symbol": asset_code, "amount": 3}

    response = client.add_extra_data_token({"uid": user_id}).post(
        "/toro/order", data=dumps(payload)
    )

    response_data = response.json()

    assert response.status_code == HTTPStatus.OK
    assert response_data["order"] is not None
