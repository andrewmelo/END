from sqlalchemy import Column, Integer, BigInteger, Boolean
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base

from database import get_session


Base = declarative_base()

session = get_session()


class AccountModel(Base):
    __tablename__ = "accounts"
    user_id = Column(BigInteger, primary_key=True, nullable=False)
    checking = Column(Integer, default=0)
    savings = Column(Integer, default=0)
    stashed = Column(Integer, default=0)
    is_open = Column(Boolean, default=True)
    time_until_daily_reward = Column(Integer, default=0)

    def open_account(self, user_id):
        try:
            self.account = AccountModel(
                user_id=user_id
            )
            session.add(self.account)
            session.commit()
        except SQLAlchemyError as e:
            print(e)

    def deposit(self):
        pass

    def withdraw(self):
        pass