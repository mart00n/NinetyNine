from random import shuffle

class Deck:
    """Deck of cards"""
    def __init__(self):
        self.deck = list(range(100))
        shuffle(self.deck)

    def draw(self):
        if len(self.deck) > 0:
            return self.deck.pop()
        else:
            raise ValueError()

# d = Deck()

# for n in range(101):
#     print(d.draw())
#     print(len(d.deck))