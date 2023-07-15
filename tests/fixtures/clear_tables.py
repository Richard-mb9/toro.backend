import pytest
from src.domain import Account, User, Asset
from src.infra.configs import DBConnectionHandler


def delete_items(entity):
    session = DBConnectionHandler().get_session()
    list = session.query(entity).filter().all()
    for item in list:
        session.delete(item)

    session.commit()


@pytest.fixture(scope="function")
def clear_all_tables():
    yield
    delete_items(Account)
    delete_items(User)
    delete_items(Asset)
