from .base_reposiitory import BaseRepository
from src.domain import Account


class AccountsRepository(BaseRepository):
    def __init__(self):
        super().__init__(Account)

    def find_by_user_id(self, user_id: int) -> Account | None:
        return self.session.query(self.entity).filter_by(user_id=user_id).first()
