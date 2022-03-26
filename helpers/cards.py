from random import choice
from rpgtk.cards import Card, Deck

from sources.decks import DECKS

setattr(Card, 'is_upside_down', 'No')

def get_three_cards(selected_deck):
    deck_list = DECKS[selected_deck]
    card_list = []
    reading = Deck()

    for key, value in deck_list.items():
        card_list.append(Card({key: value}))

    deck = Deck(card_list)

    deck.shuffle()

    for card in range(3):
        reading.pack(deck.draw())
        reading.cards[card].is_upside_down = choice(['Yes', 'No'])

    return reading
