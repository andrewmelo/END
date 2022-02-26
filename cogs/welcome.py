from discord.ext import commands

from models.player_model import base
from database import get_session

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
        base.metadata.drop_all(session.bind)
        base.metadata.create_all(session.bind)
        

def setup(bot):
    bot.add_cog(MainCog(bot))
