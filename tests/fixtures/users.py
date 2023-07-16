from json import dumps
import pytest
from .app import Client

USERS = [
    {
        "name": "Avery",
        "email": "Avery50@outlook.com.br",
        "password": "12345678",
        "cpf": "12345679010",
    },
    {
        "Mia": "Avery",
        "email": "Mia30@terra.com.br",
        "password": "12345678",
        "cpf": "12345679011",
    },
    {
        "Mia": "Emily",
        "email": "Emily1950@outlook.org",
        "password": "12345678",
        "cpf": "12345679012",
    },
]


def transfer(client: Client, user_id, cpf):
    account_response = client.add_extra_data_token({"uid": user_id}).get(
        "/toro/users/account"
    )

    account_data = account_response.json()
    account = account_data["account"]

    payload = {
        "event": "TRANSFER",
        "target": {"bank": "352", "branch": "0001", "account": account},
        "origin": {"bank": "033", "branch": "03312", "cpf": cpf},
        "amount": 1000,
    }

    client.post("/toro/spb/events", data=dumps(payload))


@pytest.fixture
def users(client: Client, clear_all_tables):
    for user in USERS:
        client.post("/toro/users", data=dumps(user))
