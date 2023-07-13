from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session as SessionType

from src.config import HOST_DB, PASSWORD_DB, USER_DB, NAME_DB, PORT_DB


class DBConnectionHandler:
    """SQLAlchemy database connection"""

    def __init__(self):
        self.url_db = (
            f"mysql+pymysql://{USER_DB}:{PASSWORD_DB}@{HOST_DB}:{PORT_DB}/{NAME_DB}"
        )
        self.session = None

    def get_session(self) -> SessionType:
        engine = create_engine(self.url_db)
        Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        session: SessionType = Session()
        return session
