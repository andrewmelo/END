from discord import Embed
from discord.ext import commands
from discord_slash import cog_ext, SlashContext

class CharacterCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="listcharacters",)
    async def listcharacters(self, ctx: SlashContext):
        """Show list of owned characters."""
        await ctx.send("List of your characters:")


def setup(bot):
    bot.add_cog(CharacterCog(bot))
