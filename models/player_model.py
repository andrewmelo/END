from datetime import datetime
from discord import Embed
from sqlalchemy import Integer, BigInteger, DateTime, Column
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base

from constants import COIN, BAG
from database import get_session
from .account_model import AccountModel


Base = declarative_base()

session = get_session()


class PlayerModel(Base):
    __tablename__ = 'players'
    user_id = Column(BigInteger, primary_key=True, nullable=False)
    currency = Column(Integer, default=10)
    created_at = Column(DateTime, default=datetime.utcnow())

    def create(self, user_id):
        try:
            self.player = PlayerModel(
                user_id=user_id
            )
            session.add(self.player)
            session.commit()
            account = AccountModel()
            account.open_account(self.player.user_id)
        except SQLAlchemyError as e:
            print(e)

    def get_info(self, user_id):
        try:
            self.player = session.query(PlayerModel).get(user_id)
            if self.player == None:                
                return None
            else:
                return self.player
        except SQLAlchemyError as e:
            print(e)

    def show(self, nick, avatar_url):
        embed = Embed(colour=0x7833bd)
        embed.set_author(name=nick, icon_url=avatar_url)
        embed.add_field(name=COIN, value=self.currency, inline=True)
        embed.add_field(name=BAG, value="Empty", inline=True)
        return embed

    def update():
        pass

    def delete():
        pass