from discord.ext import commands
from discord_components import Select, SelectOption
from helpers import cards

from sources.decks import DECK_OPTIONS

class DiceCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=['tcr'])
    async def threecardreading(self, ctx):
        """Gives you options for card reading"""
        async def callback(interaction):
            reading = cards.three_card_reading(interaction.values[0])
            await interaction.send(content=f'You chose: {interaction.values[0]}', embed=reading, ephemeral=False)
            await msg.delete()

        msg = await ctx.send(
            "Choose a deck:",
            components = [
                self.bot.components_manager.add_callback(
                    Select(options=DECK_OPTIONS),
                    callback,
                    uses=1
                )
            ],
        )

def setup(bot: commands.Bot):
    bot.add_cog(DiceCommands(bot))