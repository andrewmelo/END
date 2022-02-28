from datetime import datetime
from discord import Embed
from sqlalchemy import Integer, BigInteger, DateTime, Column
from sqlalchemy.exc import SQLAlchemyError

from constants import COIN, BAG
from database import Base
from database.session_handler import get_object


class PlayerModel(Base):
    __tablename__ = 'players'
    user_id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=False)
    currency = Column(Integer, default=10)
    created_at = Column(DateTime, default=datetime.utcnow())
    
    @classmethod
    def get_player(cls, user_id):
        try:
            return get_object(cls, user_id=user_id)
        except SQLAlchemyError as e:
            print(e)

    def show(self, nick, avatar_url):
        embed = Embed(color=0x7833bd)
        embed.set_author(name=nick, icon_url=avatar_url)
        embed.add_field(name=COIN, value=self.currency, inline=True)
        embed.add_field(name=BAG, value="Empty", inline=False)
        return embed

    def update():
        pass

    def delete():
        pass