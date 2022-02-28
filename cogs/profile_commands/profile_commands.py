from discord import Embed
from discord.ext import commands

from constants import PREFIX
from models.player_model import PlayerModel
from models.account_model import AccountModel
from database.session_handler import save_object

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
            account = AccountModel(user_id=player.user_id)
            save_object(account)
            await ctx.send("You got 10 coins for creating your profile! "
                            "Don't spent them all in one place. You should "
                            f"try {PREFIX}bankaccount to check what you can "
                            "do with all that money.")
        embed = player.show(
            nick=ctx.author.nick,
            avatar_url=ctx.author.avatar_url
        )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(MainCog(bot))
