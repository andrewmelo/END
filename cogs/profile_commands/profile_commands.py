from datetime import datetime as dt
from db_connect import cursor
from discord import Embed
from discord.ext import commands
from mariadb import Error
from config import FETCH_PLAYERS_ALL


class MainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=['dp'])
    async def discordprofile(self, ctx):
        """Setup or show discord profile"""
        try:
            embed = Embed(colour=0x7833bd)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            embed.add_field(name='Nick', value=ctx.author.nick, inline=True)
            roles_list = []
            for x in ctx.author.roles:
                if x.name != '@everyone':
                    roles_list.append(x.name)
            role = ', '.join(roles_list)
            embed.add_field(name='Roles', value=role)
            await ctx.send(embed=embed)
        except Exception as e:
            print(e)
            return
    
    @commands.command(aliases=['p'])
    async def profile(self, ctx):
        """Setup or show player profile"""
        try:         
            #cursor.execute('SELECT PlayerID FROM Players WHERE PlayerID=?', (ctx.author.id,))
            cursor.execute(FETCH_PLAYERS_ALL, ('testeid',))
            player_info = cursor.fetchone()
            author_id = []
            for i in player_info.values():
                author_id.append(i)
            if author_id[0] == 'testeid':
                pass
            else:
                pass
        except Error as e:
            print(e)
            return

def setup(bot):
    bot.add_cog(MainCog(bot))
