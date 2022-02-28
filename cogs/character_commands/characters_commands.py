from discord import Embed
from discord.ext import commands


class MainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["lc"])
    async def listcharacters(self, ctx):
        """Show discord profile"""
        pass


def setup(bot):
    bot.add_cog(MainCog(bot))
