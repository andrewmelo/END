from discord.ext import commands

from helpers.cards import get_deck


class DiceCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=['tcr'])
    async def threecardreading(self, ctx):
        """Gives you a three card reading"""
        deck = get_deck()
        deck.shuffle()
        cards = []
        for card in range(3):
            cards.append(deck.draw())
        await ctx.send(
            f"\nFirst card: {cards[0]}"
            f"\nSecond card: {cards[1]}"
            f"\nThird card: {cards[2]}"
            )


def setup(bot: commands.Bot):
    bot.add_cog(DiceCommands(bot))