from discord.ext import commands
from discord import utils

from models.account_model import AccountModel

class MainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=["ba"])
    async def bankaccount(self, ctx):
        bank_statement = AccountModel()        
        embed = bank_statement.get_info(
            ctx.author.id,
            ctx.author.nick,
            ctx.author.avatar_url,
        )
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(MainCog(bot))
