from random import shuffle

from sources.decks import DECKS

def get_three_cards(selected_deck):
    deck = DECKS[selected_deck]
    deck_list = []
    cards = []
    urls = []

    for key in deck:
        deck_list.append(key)
    
    shuffle(deck_list)

    for card in range(3):
        cards.append(deck_list[card])
        urls.append(deck[deck_list[card]])

    reading = dict(zip(cards, urls))
    return reading
