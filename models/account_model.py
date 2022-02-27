from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

from constants import COIN, BAG
from database import get_session

base = declarative_base()

session = get_session()


class AccountModel(base):
    __tablename__ = "accounts"
    user_id = Column(String(length=30), primary_key=True, nullable=False)