from database import get_session
from discord.ext import commands
from rpgtk.core import Dice
from rpgtk.exceptions import DiceException
from sqlalchemy.exc import SQLAlchemyError

from helpers.dice_roller import Bet
from models.player_model import PlayerModel

class DiceCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=['r'])
    async def roll(self, ctx, sides):
        """Rolls a custom die."""
        try:
            dice = Dice(int(sides))
        except (DiceException, ValueError):
            await ctx.send("Valor inválido.")
            return
        await ctx.send("Resultado: {result}".format(result=dice.roll()))

    @commands.command()
    async def d6(self, ctx, qtd):
        """Rolls a custom die."""
        try:
            dice = Dice()
            result = []
            for r in range(int(qtd)):
                result.append(dice.roll())
        except (DiceException, ValueError):
            await ctx.send("Valor inválido.")
            return
        await ctx.send(f"Resultado: {result}")

    @commands.command(aliases=['bet'])
    async def dicebet(self, ctx, money):
        session = get_session()
        player = PlayerModel.get_player(ctx.author.id)
        if player:
            if player.checking_account >= int(money) and int(money) != 0:
                bet = Bet()
                bet.bet(int(money))   
                if bet.reward > 0:
                    player.checking_account += bet.reward
                    session.commit()
                    await ctx.send(
                        f"\nYou rolled: {bet.player_roll}"
                        f"\nThe dealer rolled: {bet.results}"
                        f"\nYour reward: {bet.reward}"
                        f"\nChecking account: {player.checking_account}"
                    )
                else:
                    player.checking_account -= int(money)
                    session.commit()
                    await ctx.send(
                        "Better luck next time!"
                        f"\nYou rolled: {bet.player_roll}"
                        f"\nThe dealer rolled: {bet.results}"
                        f"\nChecking account: {player.checking_account}"
                    )
            else:
                await ctx.send("You don't have enough to bet.")
        else:
            await ctx.send("You don't have an account yet.")
        

def setup(bot: commands.Bot):
    bot.add_cog(DiceCommands(bot))