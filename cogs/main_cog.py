from discord.ext import commands
from sqlalchemy import create_engine

from config import ENGINE_URL
from database import Base


class MainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot
        print("Logged in as {0.user}".format(self.bot))

    @commands.command()
    async def setupdb(self, ctx):
        engine = create_engine(ENGINE_URL)
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        print("Executado")

    @commands.command(aliases=["h", "çocorro"])
    async def help(self, ctx):
        await ctx.send("HELP")


def setup(bot):
    bot.add_cog(MainCog(bot))
