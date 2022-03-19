from rpgtk.cards import Deck, Card
from constants import CARDS_DESCRIPTION


def get_deck():
    deck = Deck(default=True)
    setattr(Card, 'description', 'No description given.')
    for i, card in enumerate(deck.cards):
        card.description = CARDS_DESCRIPTION[i]
    return deck