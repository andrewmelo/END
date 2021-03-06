from datetime import datetime
from discord import Embed
from sqlalchemy import Integer, BigInteger, DateTime, Column
from sqlalchemy.exc import SQLAlchemyError

from database import Base
from database.session_handler import select_one_from


class PlayerModel(Base):
    __tablename__ = 'players'
    user_id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=False)
    created_at = Column(DateTime, default=datetime.utcnow())
    checking_account = Column(Integer, default=10)
    savings_account = Column(Integer, default=0)
    stashed_cash = Column(Integer, default=0)
    last_daily_claim = Column(DateTime, default=datetime.utcnow())
    last_bet = Column(DateTime, default=datetime.utcnow())

    @classmethod
    def get_player(cls, user_id):
        try:
            return select_one_from(cls, user_id=user_id)
        except SQLAlchemyError as e:
            print(e)


    def show(self, nick, avatar_url, currency, savings):
        embed = Embed(color=0x7833bd)
        embed.set_author(name=nick, icon_url=avatar_url)
        embed.insert_field_at(0, name='Currency', value=currency, inline=True)
        embed.insert_field_at(1, name='Savings', value=savings, inline=True)
        embed.set_footer(text=':p')
        return embed
