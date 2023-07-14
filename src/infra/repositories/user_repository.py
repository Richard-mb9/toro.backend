from .base_reposiitory import BaseRepository
from src.domain import User


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(User)

    def find_by_id(self, id: int) -> User | None:
        return self.session.query(self.entity).filter_by(id=id).first()

    def find_by_email(self, email: str) -> User | None:
        return self.session.query(self.entity).filter_by(email=email).first()

    def find_by_cpf(self, cpf: str) -> User | None:
        return self.session.query(self.entity).filter_by(cpf=cpf).first()

    def update(self, id, data_to_update: dict):
        entity = self.find_by_id(id)
        for key in data_to_update:
            if data_to_update[key] is not None:
                setattr(entity, key, data_to_update[key])
        self.session.commit()
        return entity
