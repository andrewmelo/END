from datetime import datetime
from discord import Embed
from sqlalchemy import Integer, BigInteger, DateTime, String, Column, ForeignKey
from sqlalchemy.exc import SQLAlchemyError

from database import Base
from database.session_handler import get_object


class LAFModel(Base):
    """Model for Lasers And Feelings system"""
    __tablename__ = 'laser_and_feelings'
    character_id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    character_name = Column(String(30), nullable=False)
    style = Column(String(15))
    role = Column(String(15))
    number = Column(Integer)
    goal = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow())
    user_id = Column(BigInteger, ForeignKey('players.user_id'))
    
    @classmethod
    def get_character(cls, user_id):
        try:
            return get_object(cls, user_id=user_id)
        except SQLAlchemyError as e:
            print(e)

    def new_character(cls):
        pass