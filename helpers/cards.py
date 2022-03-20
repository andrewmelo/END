from discord.embeds import Embed
from random import shuffle

from sources.decks import DECKS


def three_card_reading(selected_deck):
    deck = DECKS[selected_deck]
    shuffle(deck)
    results = []
    for card in range(3):
        results.append(deck[card])
    embed = Embed()
    embed.add_field(name='Past', value=results[0], inline=False)
    embed.add_field(name='Present', value=results[1], inline=False)
    embed.add_field(name='Future', value=results[2], inline=False)
    return embed
    