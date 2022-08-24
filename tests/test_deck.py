from ninetynine.deck import Deck
def test_draw_returns_int():
    deck = Deck()
    card = deck.draw()
    assert isinstance(card, int)

def test_draw_removes_from_deck():
    deck = Deck()
    for n in range(5):
        deck.draw()
    assert len(deck.deck) == 95

def test_cannot_draw_from_empty_deck():
    deck = Deck()
    for n in range(101):
        try:
            deck.draw()
        except ValueError:
            return True
    assert False