import pytest
from src.infra.repositories import AssetsRepository
from src.domain import Asset

ASSETS_DATA = [
    {"code": "MGLU3", "name": "Magazine Luiza", "price": 2.98},
    {"code": "VIIA3", "name": "Via", "price": 1.96},
    {"code": "HAPV3", "name": "Hapvida", "price": 4.34},
    {"code": "PETR4", "name": "Petrobras", "price": 29.17},
    {"code": "B3SA3", "name": "B3", "price": 14.25},
    {"code": "JBSS3", "name": "JBS", "price": 18.80},
    {"code": "VALE3", "name": "Vale", "price": 67.05},
    {"code": "BBDC4", "name": "Banco Bradesco", "price": 16.15},
    {"code": "CIEL3", "name": "Cielo", "price": 4.52},
    {"code": "ITUB4", "name": "Itaú Unibanco", "price": 28.27},
]


@pytest.fixture
def assets(clear_all_tables):
    repository = AssetsRepository()
    for asset in ASSETS_DATA:
        new_asset = Asset(code=asset["code"], name=asset["name"], price=asset["price"])
        repository.insert(new_asset)
