from discord import Embed
from discord.ext import commands

class CharacterCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['lc'])
    async def listcharacters(self, ctx):
        """Show list of owned characters."""
        await ctx.send("List of your characters:")


def setup(bot):
    bot.add_cog(CharacterCog(bot))
