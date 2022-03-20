from copy import deepcopy
from discord.ext import commands
from sqlalchemy import create_engine
from discord.ext.commands import CommandNotFound

from config import ENGINE_URL
from database import Base


class MainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot
        print("Logged in as {0.user}".format(self.bot))

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, CommandNotFound):
            return
        raise error;

    @commands.command()
    async def setupdb(self, ctx, *args):
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

    @commands.command()
    async def setupdball(self, ctx):
        engine = create_engine(ENGINE_URL)
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        await ctx.send("Todas as tablelas resetadas.")

    @commands.command()
    async def help(self, ctx):
        await ctx.send("HELP")

    @commands.command()
    async def test(self, ctx):
        await ctx.send("Teste concluído.")

def setup(bot):
    bot.add_cog(MainCog(bot))
