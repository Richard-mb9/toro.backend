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

    def format_search_query(self, result):
        columns = [desc[0] for desc in result.cursor.description]
        datas = []
        for item in result:
            i = 0
            data = {}
            for col in columns:
                data[col] = item[i]
                i += 1
            datas.append(data)
        return datas
