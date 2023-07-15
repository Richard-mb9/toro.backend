from src.infra.repositories import AccountsRepository
from src.domain import Account


class AccountsService:
    """Class Accounts Service"""

    def __init__(self):
        self.repository = AccountsRepository()

    def create_account(self, user_id):
        account = Account(user_id=user_id)
        account_created = self.repository.insert(account)
        return {"id": account_created.id}

    def find_by_user_id(self, user_id: int):
        return self.repository.find_by_user_id(user_id)
