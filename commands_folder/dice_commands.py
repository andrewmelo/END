from discord.ext import commands
from rpgtk.core import Dice
from rpgtk.exceptions import DiceException


class DiceComm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, ctx, arg):
        try:
            dice = Dice(int(arg))
        except (DiceException, ValueError):
            await ctx.send("Valor inválido.")
            return
        await ctx.send("Resultado: {result}".format(result=dice.roll()))
