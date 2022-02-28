from discord.ext import commands
from rpgtk.core import Dice
from rpgtk.exceptions import DiceException

from helpers.dice_roller import Bet


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

    @commands.command(aliases=["bet"])
    async def dicebet(self, ctx, money):
        bet = Bet()
        bet.bet(int(money))
        
        await ctx.send(
            f"\nYou rolled: {bet.player_roll}"
            f"\nThe dealer rolled: {bet.results}"
            f"\nYour reward: {bet.reward}"
        )

def setup(bot):
    bot.add_cog(DiceCommands(bot))