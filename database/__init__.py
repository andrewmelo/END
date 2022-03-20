from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config import ENGINE_URL


Base = declarative_base()

def get_session():
    session = sessionmaker(my_create_engine())
    return session()

def my_create_engine():
    return create_engine(ENGINE_URL, pool_size=5, max_overflow=5)
