from .base_reposiitory import BaseRepository
from src.domain import Account


class AccountsRepository(BaseRepository):
    def __init__(self):
        super().__init__(Account)
