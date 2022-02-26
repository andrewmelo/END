from discord import Embed
from discord.ext import commands

from models.player_model import PlayerModel

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
        player = PlayerModel()
        player = player.get_info(ctx.author.id)
        if player == None:
            player = PlayerModel()
            player.create(ctx.author.id)
        elif str(ctx.author.id) == str(player.user_id):
            embed = player.show(
                nick=ctx.author.nick,
                avatar_url=ctx.author.avatar_url
            )
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(MainCog(bot))
