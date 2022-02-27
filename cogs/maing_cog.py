from discord.ext import commands

from database import get_session
from models.account_model import Base as AccountBase
from models.player_model import Base as PlayerBase


class MainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot
        print("Logged in as {0.user}".format(self.bot))

    @commands.command()
    async def setupdb(self, ctx):

        session = get_session()
        session.close_all()
        AccountBase.metadata.drop_all(session.bind)
        PlayerBase.metadata.drop_all(session.bind)
        AccountBase.metadata.create_all(session.bind)
        PlayerBase.metadata.create_all(session.bind)


def setup(bot):
    bot.add_cog(MainCog(bot))
