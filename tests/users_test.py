# pylint: disable=W0613

from json import dumps
from http import HTTPStatus
from copy import deepcopy

from tests.fixtures.app import Client
from src.services import UserService
from src.services import AccountsService

DEFAULT_USER = {
    "name": "Ricardo",
    "email": "ricardo@dom.com",
    "password": "123456789",
    "cpf": "15012345610",
}


def test_should_create_a_user(client: Client, clear_all_tables):
    response = client.post("/toro/users", data=dumps(DEFAULT_USER))
    assert response.status_code == HTTPStatus.CREATED

    user_created = UserService().find_by_id(response.json()["id"])
    assert user_created is not None
    assert user_created.cpf == DEFAULT_USER["cpf"]


def test_not_should_create_duplicate_user(client: Client, clear_all_tables):
    client.post("/toro/users", data=dumps(DEFAULT_USER))
    response = client.post("/toro/users", data=dumps(DEFAULT_USER))
    assert response.status_code == HTTPStatus.CONFLICT


def test_should_not_allow_creating_invalid_passwords(client: Client, clear_all_tables):
    user = deepcopy(DEFAULT_USER)
    user["password"] = "123456"
    response = client.post("/toro/users", data=dumps(user))
    assert response.status_code == HTTPStatus.BAD_REQUEST

    response_data = response.json()
    assert response_data["detail"]["error"] == "password must contain at least 8 digits"

    user["password"] = "123abc3gf3j6l9o844eo533p32"
    response = client.post("/toro/users", data=dumps(user))
    assert response.status_code == HTTPStatus.BAD_REQUEST

    response_data = response.json()
    assert (
        response_data["detail"]["error"]
        == "The password must contain a maximum of 24 characters"
    )


def test_should_not_allow_to_use_invalid_cpf(client: Client, clear_all_tables):
    user = deepcopy(DEFAULT_USER)
    user["cpf"] = "abcdef123456"

    response = client.post("/toro/users", data=dumps(user))
    assert response.status_code == HTTPStatus.BAD_REQUEST

    response_data = response.json()
    assert response_data["detail"]["error"] == "Invalid CPF"

    user["cpf"] = "123"

    response = client.post("/toro/users", data=dumps(user))
    assert response.status_code == HTTPStatus.BAD_REQUEST

    response_data = response.json()
    assert response_data["detail"]["error"] == "Invalid CPF"


def test_should_not_allow_to_use_invalid_email(client: Client, clear_all_tables):
    user = deepcopy(DEFAULT_USER)
    user["email"] = "ricardo@dom"

    response = client.post("/toro/users", data=dumps(user))
    assert response.status_code == HTTPStatus.BAD_REQUEST

    response_data = response.json()
    assert response_data["detail"]["error"] == "Invalid email"

    user["email"] = "ricardo.com"

    response = client.post("/toro/users", data=dumps(user))
    assert response.status_code == HTTPStatus.BAD_REQUEST

    response_data = response.json()
    assert response_data["detail"]["error"] == "Invalid email"


def test_should_create_an_account_for_the_created_user(
    client: Client, clear_all_tables
):
    response = client.post("/toro/users", data=dumps(DEFAULT_USER))

    response_data = response.json()

    account = AccountsService().find_by_user_id(response_data["id"])

    assert account is not None


def test_should_update_the_user(client: Client, clear_all_tables):
    response = client.post("/toro/users", data=dumps(DEFAULT_USER))

    response_data = response.json()
    user_id = response_data["id"]

    new_data = {"name": "other"}

    response = client.add_extra_data_token({"uid": user_id}).put(
        "/toro/users", data=dumps(new_data)
    )

    assert response.status_code == HTTPStatus.OK

    user = UserService().find_by_id(user_id)
    assert user.name == new_data["name"]


def test_should_update_the_user_password(client: Client, clear_all_tables):
    user = deepcopy(DEFAULT_USER)
    current_password = "12345678"
    user["password"] = current_password

    response = client.post("/toro/users", data=dumps(user))
    response_data = response.json()
    user_id = response_data["id"]

    new_password = "987654321"

    data = {"current_password": current_password, "new_password": new_password}

    response = client.add_extra_data_token({"uid": user_id}).put(
        "/toro/users/password", data=dumps(data)
    )

    assert response.status_code == HTTPStatus.OK

    user_updated = UserService().find_by_id(user_id)
    assert user_updated.password == UserService().encode_password(new_password)


def test_should_not_update_the_user_password_if_current_password_is_incorrect(
    client: Client, clear_all_tables
):
    user = deepcopy(DEFAULT_USER)
    user["password"] = "12345678"

    response = client.post("/toro/users", data=dumps(user))
    response_data = response.json()
    user_id = response_data["id"]

    new_password = "987654321"

    data = {"current_password": "incorrect_password", "new_password": new_password}

    response = client.add_extra_data_token({"uid": user_id}).put(
        "/toro/users/password", data=dumps(data)
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    response_data = response.json()
    assert response_data["detail"]["error"] == "incorrect password"


def test_validate_if_the_new_password_is_the_same_as_the_old_one(
    client: Client, clear_all_tables
):
    user = deepcopy(DEFAULT_USER)
    current_password = "12345678"
    user["password"] = current_password

    response = client.post("/toro/users", data=dumps(user))
    response_data = response.json()
    user_id = response_data["id"]

    data = {"current_password": current_password, "new_password": current_password}

    response = client.add_extra_data_token({"uid": user_id}).put(
        "/toro/users/password", data=dumps(data)
    )

    response_data = response.json()

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert (
        response_data["detail"]["error"]
        == "the new password cannot be the same as the current password"
    )


def test_should_not_allow_update_password_with_invalid_passwords(
    client: Client, clear_all_tables
):
    user = deepcopy(DEFAULT_USER)
    current_password = "12345678"
    user["password"] = current_password

    response = client.post("/toro/users", data=dumps(user))
    response_data = response.json()
    user_id = response_data["id"]

    data = {"current_password": current_password, "new_password": "invalid"}
    response = client.add_extra_data_token({"uid": user_id}).put(
        "/toro/users/password", data=dumps(data)
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST

    response_data = response.json()
    assert response_data["detail"]["error"] == "password must contain at least 8 digits"

    data = {
        "current_password": current_password,
        "new_password": "123abc3gf3j6l9o844eo533p32",
    }
    response = client.add_extra_data_token({"uid": user_id}).put(
        "/toro/users/password", data=dumps(data)
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST

    response_data = response.json()
    assert (
        response_data["detail"]["error"]
        == "The password must contain a maximum of 24 characters"
    )
