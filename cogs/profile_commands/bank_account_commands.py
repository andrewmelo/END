from discord.ext import commands
from discord_slash import cog_ext, SlashContext

from models.bank_account_model import BankAccountModel
from database.session_handler import get_object

class BankAccountCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @cog_ext.cog_slash(name="bankaccount")
    async def bankaccount(self, ctx: SlashContext):
        account = get_object(BankAccountModel, user_id=ctx.author.id)
        if account:
            embed = account.get_info_embed(
                ctx.author.nick,
                ctx.author.avatar_url,
            )
            await ctx.send(embed=embed)

    @cog_ext.cog_slash(name="dailyreward")
    async def dailyreward(self, ctx: SlashContext):
        pass

def setup(bot):
    bot.add_cog(BankAccountCog(bot))
