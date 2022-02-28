from datetime import datetime
from discord import Embed
from sqlalchemy import Column, Integer, BigInteger, Boolean, DateTime
from sqlalchemy.exc import SQLAlchemyError

from constants import COIN, DAILY_CLAIM
from database import Base
from database.session_handler import get_object


class AccountModel(Base):
    __tablename__ = "accounts"
    user_id = Column(BigInteger, primary_key=True, nullable=False)
    checking = Column(Integer, default=10)
    savings = Column(Integer, default=0)
    stashed = Column(Integer, default=0)
    is_open = Column(Boolean, default=True)
    last_daily_claim = Column(DateTime, default=None)

    def get_info_embed(self, nick, avatar_url):
        today = datetime.utcnow()
        embed = Embed(title="Accounts", color=0x128a33)
        embed.set_author(
            name="💰 Bank"                    
        )
        embed.set_footer(text=nick, icon_url=avatar_url)
        embed.add_field(
            name="Checking",
            value=f"{self.checking} {COIN}",
            inline=True
        )
        embed.add_field(
            name="Savings",
            value=f"{self.savings} {COIN}",
            inline=True
        )
        if (
            self.last_daily_claim is None
            or DAILY_CLAIM >= today - self.last_daily_claim
        ):
            embed.add_field(
                name="Daily Reward",
                value="Avalilable: $dr",
                inline=False
            )
        else:
            embed.add_field(
                name="Daily Reward",
                value="Not available yet",
                inline=False
            )
        return embed
    
    @classmethod
    def get_account(cls, user_id):
        try:
            return get_object(cls, user_id=user_id)
        except SQLAlchemyError as e:
            print(e)