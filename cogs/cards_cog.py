from discord import Embed
from discord.ext import commands
from discord_components import Select, Button, ButtonStyle, ActionRow

from helpers import cards
from sources.decks import DECK_OPTIONS

class DiceCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=['tcrs'])
    async def threecardreadingsimple(self, ctx):
        """Gives you options for card reading"""
        async def callback(interaction):
            reading = cards.get_three_cards(str(interaction.values[0]))
            r_cards = []
            for key in reading:
                r_cards.append(key)
            embed = Embed(title=f'Your reading from {interaction.values[0]} deck:')
            embed.add_field(name='First card:', value=r_cards[0], inline=True)
            embed.add_field(name='Second card:', value=r_cards[1], inline=True)
            embed.add_field(name='Third card:', value=r_cards[2], inline=True)
            await interaction.send(embed=embed, ephemeral=False)
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

    @commands.command(aliases=['tcr'])
    async def threecardreading(self, ctx):
        """Gives you options for card reading"""
        async def callback(interaction):
            reading = cards.get_three_cards(interaction.values[0])
            cartas = []
            urls = []
            current_card = 0
            for key in reading:
                cartas.append(key)
                urls.append(reading[key])
            embed = Embed(title=cartas[current_card])
            if urls[current_card] is not None:
                embed.set_image(url=str(urls[current_card]))
            
            embed_list = Embed(title=f'Your reading from {interaction.values[0]} deck:')
            embed_list.add_field(name='First card:', value=cartas[0], inline=True)
            embed_list.add_field(name='Second card:', value=cartas[1], inline=True)
            embed_list.add_field(name='Third card:', value=cartas[2], inline=True)

            botoes = ActionRow([
                Button(style=ButtonStyle.gray, label='Previous', custom_id='previous'),
                Button(style=ButtonStyle.gray, label='Next', custom_id='next'),
                Button(style=ButtonStyle.gray, label='List', custom_id='list_cards'),
            ])
            msg2 = await interaction.send(embed=embed, ephemeral=False, components=botoes)
            await msg.delete()

            while True:
                moderator = await self.bot.wait_for('button_click')
                if moderator.component.label == 'Previous':
                    if current_card > 0:
                        current_card -= 1
                        embed.title = cartas[current_card]
                        embed.set_image(url=urls[current_card])
                        await msg2.edit(embed=embed)
                    else:
                        current_card = len(cartas) - 1
                    try:
                        await moderator.respond()
                    except:
                        pass

                if moderator.component.label == 'Next':
                    if current_card < len(cartas) - 1:
                        current_card += 1
                        embed.title = cartas[current_card]
                        embed.set_image(url=urls[current_card])
                        await msg2.edit(embed=embed)
                    else:
                        current_card = 0
                    try:
                        await moderator.respond()
                    except:
                        pass

                if moderator.component.label == 'List':
                    await msg2.edit(embed=embed_list)
                    try:
                        await moderator.respond()
                    except:
                        pass

        msg = await ctx.send(
            "Chose a deck:",
            components = [
                self.bot.components_manager.add_callback(
                    Select(options=DECK_OPTIONS),
                    callback,
                    uses=1
                )
            ],
        )

    @commands.command()
    async def button(self, ctx):
        async def callback(interaction):
            await interaction.send(content="Yay")

        await ctx.send(
            "Button callbacks!",
            components=[
                self.bot.components_manager.add_callback(
                    Button(style=ButtonStyle.blue, label="Click this"), callback
                ),
            ],
        )

def setup(bot: commands.Bot):
    bot.add_cog(DiceCommands(bot))