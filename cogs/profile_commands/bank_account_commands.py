from discord.ext import commands

from models.bank_account_model import BankAccountModel
from database.session_handler import get_object

class MainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=["ba"])
    async def bankaccount(self, ctx):
        account = get_object(BankAccountModel, user_id=ctx.author.id)
        if account:
            embed = account.get_info_embed(
                ctx.author.nick,
                ctx.author.avatar_url,
            )
            await ctx.send(embed=embed)

    @commands.command(aliases=["dr"])
    async def dailyreward(self, ctx):
        pass

def setup(bot):
    bot.add_cog(MainCog(bot))
