from sqlalchemy import create_engine
from sqlalchemy import orm

from config import ENGINE_URL


engine = create_engine(ENGINE_URL, echo=True, future=True)


def get_session():
    session = orm.sessionmaker()
    session.configure(bind=engine)
    session = session()
    return session
