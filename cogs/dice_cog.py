from discord.ext import commands
from rpgtk.core import Dice
from rpgtk.exceptions import DiceException
from discord_slash import cog_ext, SlashContext

from helpers.dice_roller import Bet
from models.bank_account_model import BankAccountModel
from database.session_handler import transaction


class DiceCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @cog_ext.cog_slash(
        name="roll",
        description="Roll a dice with the number of sides informed."
    )
    async def roll(self, ctx: SlashContext, sides):
        """Rolls a custom die."""
        try:
            dice = Dice(int(sides))
        except (DiceException, ValueError):
            await ctx.send("Valor inválido.")
            return
        await ctx.send("Resultado: {result}".format(result=dice.roll()))

    @cog_ext.cog_slash(name="dicebet")
    async def dicebet(self, ctx, money):
        bank_account = BankAccountModel.get_account(ctx.author.id)
        if bank_account:
            if bank_account.checking >= int(money) and int(money) != 0:
                bet = Bet()
                transaction(bank_account, int(money), "withdraw")
                bet.bet(int(money))   
                if bet.reward > 0:    
                    transaction(bank_account, bet.reward, "deposit")
                    await ctx.send(
                        f"\nYou rolled: {bet.player_roll}"
                        f"\nThe dealer rolled: {bet.results}"
                        f"\nYour reward: {bet.reward}"
                        f"\nChecking account: {bank_account.checking}"
                    )
                else:
                    await ctx.send(
                        "Better luck next time!"
                        f"\nYou rolled: {bet.player_roll}"
                        f"\nThe dealer rolled: {bet.results}"
                        f"\nChecking account: {bank_account.checking}"
                    )
            else:
                await ctx.send("You don't have enough to bet.")
        else:
            await ctx.send("You don't have an account yet.")

def setup(bot: commands.Bot):
    bot.add_cog(DiceCommands(bot))