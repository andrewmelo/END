from discord.ext import commands

class MainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot
        print('Logged in as {0.user}'.format(self.bot))

def setup(bot):
    bot.add_cog(MainCog(bot))
