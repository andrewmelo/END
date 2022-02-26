from discord.ext import commands
from rpgtk.core import Dice
from rpgtk.exceptions import DiceException


class DiceCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, ctx, sides):
        """Rolls a custom die."""
        try:
            dice = Dice(int(sides))
        except (DiceException, ValueError):
            await ctx.send("Valor inválido.")
            return
        await ctx.send("Resultado: {result}".format(result=dice.roll()))

    #@commands.command()
    #async def roll_many(self, ctx, ):

def setup(bot):
    bot.add_cog(DiceCommands(bot))