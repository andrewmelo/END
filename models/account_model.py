from discord import Embed
from sqlalchemy import Column, Integer, BigInteger, Boolean
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base

from constants import COIN
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

    def get_info(self, user_id, nick, avatar_url):
        try:
            self.account = session.query(AccountModel).get(user_id)
            if self.account == None:
                print(f"Erro: {self.account.time_until_daily_reward}")
                return None
            else:
                embed = Embed(color=0x128a33)
                embed.set_author(name="Bank Account", icon_url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/google/313/money-bag_1f4b0.png")
                embed.set_footer(text=nick, icon_url=avatar_url)
                embed.add_field(name="Checking account", value=f"{self.account.checking} {COIN}", inline=True)
                embed.add_field(name="Savings account", value=f"{self.account.savings} {COIN}", inline=True)
                if self.account.time_until_daily_reward > 0:
                    embed.add_field(name="Daily Reward", value="Avalilable: $dr", inline=False)
                else:
                    embed.add_field(name="Daily Reward", value="Not available yet", inline=False)
                return embed
        except SQLAlchemyError as e:
            print(e)
    
    def deposit(self):
        pass

    def withdraw(self):
        pass