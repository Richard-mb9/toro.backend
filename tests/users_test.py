from json import dumps
from http import HTTPStatus

from tests.fixtures.app import Client


def test_Should_create_a_user(client: Client):
    user = {
        "name": "Ricardo",
        "email": "ricardo@dom.com",
        "password": "123456789",
        "cpf": "15012345610",
    }

    response = client.post("/toro/users", data=dumps(user))
    assert response.status_code == HTTPStatus.CREATED
