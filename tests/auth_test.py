# pylint: disable=W0613

from json import dumps
from http import HTTPStatus

from tests.fixtures.app import Client


DEFAULT_USER = {
    "name": "Ricardo",
    "email": "ricardo@dom.com",
    "password": "123456789",
    "cpf": "15012345610",
}


def test_should_be_able_to_authenticate(client: Client, clear_all_tables):
    client.post("/toro/users", data=dumps(DEFAULT_USER))

    payload = {
        "email": "ricardo@dom.com",
        "password": "123456789",
    }
    response = client.post("/toro/auth", data=dumps(payload))
    assert response.status_code == HTTPStatus.OK

    response_data = response.json()
    assert response_data["access_token"] is not None
    assert len(response_data["access_token"]) != ""


def test_should_return_an_error_if_send_invalid_credentials(
    client: Client, clear_all_tables
):
    client.post("/toro/users", data=dumps(DEFAULT_USER))

    payload = {
        "email": "ricardo@dom.com",
        "password": "incorrect_password",
    }
    response = client.post("/toro/auth", data=dumps(payload))
    assert response.status_code == HTTPStatus.UNAUTHORIZED

    response_data = response.json()
    assert response_data["detail"]["error"] == "Incorrect Credentials"

    payload = {
        "email": "incorrect@email.com",
        "password": "123456789",
    }

    response = client.post("/toro/auth", data=dumps(payload))
    assert response.status_code == HTTPStatus.UNAUTHORIZED

    response_data = response.json()
    assert response_data["detail"]["error"] == "Incorrect Credentials"
