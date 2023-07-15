from src.infra.configs import DBConnectionHandler


class BaseRepository:
    def __init__(self, entity):
        self.entity = entity
        self.session = DBConnectionHandler().get_session()

    def insert(self, entity):
        self.session.add(entity)
        self.session.commit()
        return entity

    def list(self):
        return self.session.query(self.entity).filter().all()
