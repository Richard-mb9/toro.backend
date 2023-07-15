from datetime import datetime, timedelta
from fastapi import FastAPI
from fastapi.testclient import TestClient
import jwt
import pytest
from dotenv import find_dotenv, load_dotenv
from alembic import config


from src.api.main import create_app
from src.config import SECRETKEY


class Client(TestClient):
    def __init__(self, app: FastAPI):
        super().__init__(app)
        self.token_data = {"exp": datetime.utcnow() + timedelta(minutes=5), "uid": 1}
        self.headers = {"Authorization": f"Bearer {self.__generate_token()}"}

    def get(self, url: str, headers: dict = {}, params: dict = {}):
        return super().get(url=url, headers={**self.headers, **headers}, params=params)

    def post(self, url: str, data: dict = {}, headers: dict = {}, params: dict = {}):
        return super().post(
            url=url, data=data, headers={**self.headers, **headers}, params=params
        )

    def put(self, url: str, data: dict = {}, headers: dict = {}, params: dict = {}):
        return super().put(
            url=url, data=data, headers={**self.headers, **headers}, params=params
        )

    def delete(self, url: str, headers: dict = {}, params: dict = {}):
        return super().delete(
            url=url, headers={**self.headers, **headers}, params=params
        )

    def add_extra_data_token(self, data: dict):
        self.token_data = {**self.token_data, **data}
        self.headers = {"Authorization": f"Bearer {self.__generate_token()}"}
        return self

    def __generate_token(self):
        return jwt.encode(
            self.token_data,
            key=SECRETKEY,
            algorithm="HS256",
        )


@pytest.fixture(scope="session")
def client():
    env = find_dotenv(".env.local")
    load_dotenv(env)
    app = create_app()
    config.main(argv=["--raiseerr", "upgrade", "head"])
    yield Client(app)
