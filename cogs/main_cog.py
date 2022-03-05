from copy import deepcopy
from discord.ext import commands
from discord_slash import cog_ext, SlashContext, SlashCommand
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

    @cog_ext.cog_slash(name="setupdb")
    async def setupdb(self, ctx: SlashContext, *args):
        engine = create_engine(ENGINE_URL)
        if not args:
            await ctx.send(
                "Necessário passar o nome das tableas como argumento"
            )
        else:
            Base.metadata2 = deepcopy(Base.metadata)
            for table in Base.metadata2.sorted_tables:
                for arg in args:
                    if table.name == arg:
                        Base.metadata2.remove(table) 
            Base.metadata2.drop_all(engine)
            Base.metadata2.create_all(engine)
            print("Tabelas resetadas (salvo as excluidas)")

    @cog_ext.cog_slash(name="setupdball")
    async def setupdball(self, ctx: SlashContext):
        engine = create_engine(ENGINE_URL)
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        await ctx.send("Todas as tablelas resetadas.")

    @cog_ext.cog_slash(name="help")
    async def help(self, ctx: SlashContext):
        await ctx.send("HELP")

    @cog_ext.cog_slash(name="test")
    async def test(self, ctx: SlashContext):
        await ctx.send("Teste concluído.")

def setup(bot):
    bot.add_cog(MainCog(bot))
