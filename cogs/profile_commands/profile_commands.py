from discord import Embed
from discord.ext import commands

from constants import PREFIX
from models.player_model import PlayerModel
from models.bank_account_model import BankAccountModel
from database.session_handler import save_object
from helpers.player import get_name

class MainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=["dp"])
    async def discordprofile(self, ctx):
        """Show discord profile"""
        try:
            embed = Embed(colour=0x7833bd)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            embed.add_field(name="Nick", value=ctx.author.nick, inline=True)
            roles_list = []
            for x in ctx.author.roles:
                if x.name != "@everyone":
                    roles_list.append(x.name)
            role = ", ".join(roles_list)
            embed.add_field(name="Roles", value=role)
            await ctx.send(embed=embed)
        except Exception as e:
            print(e)
            return
    
    @commands.command(aliases=["p"])
    async def profile(self, ctx):
        """Setup or show player profile"""
        player = PlayerModel.get_player(ctx.author.id)
        if not player:
            player = PlayerModel(user_id=ctx.author.id)
            save_object(player)
            bank_account = BankAccountModel(user_id=player.user_id)
            save_object(bank_account)
            await ctx.send("You got 10 coins for creating your profile! "
                            "Don't spent them all in one place. You should "
                            f"try {PREFIX}bankaccount to check what you can "
                            "do with all that money.")
        embed = player.show(
            nick=get_name(ctx),
            avatar_url=ctx.author.avatar_url
        )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(MainCog(bot))
