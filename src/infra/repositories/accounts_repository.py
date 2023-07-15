from .base_reposiitory import BaseRepository
from src.domain import Account


class AccountsRepository(BaseRepository):
    def __init__(self):
        super().__init__(Account)

    def find_by_user_id(self, user_id: int) -> Account | None:
        return self.session.query(self.entity).filter_by(user_id=user_id).first()

    def find_by_account_id(self, account_id: int) -> Account | None:
        return self.session.query(self.entity).filter_by(id=account_id).first()

    def update(self, account_id: int, data_to_update: dict):
        entity = self.find_by_account_id(account_id)
        for key in data_to_update:
            if data_to_update[key] is not None:
                setattr(entity, key, data_to_update[key])
        self.session.commit()
        return entity
