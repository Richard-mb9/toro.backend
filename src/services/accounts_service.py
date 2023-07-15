from src.infra.repositories import AccountsRepository
from src.domain import Account
from src.commons.errors import NotFoundError


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

    def find_by_account_id(self, account_id: int):
        return self.repository.find_by_account_id(account_id)

    def update(self, account_id, amount: float):
        account = self.find_by_account_id(account_id)
        if account is None:
            raise NotFoundError("Account not found")
        self.repository.update(account_id, {"amount": amount})
