class Hand:
    """Class holding cards for a single player"""
    def __init__(self, color: str):
        self.color = color
        self.cards = []
    
    def add_card(self, card: int):
        if len(self.cards) < 5:
            self.cards.append(card)
        else:
            raise ValueError('Cannot draw card, 5 cards already in hand')
    
    def remove_card(self, card: int):
        if card in self.cards:
            self.cards.remove(card)
        else:
            raise ValueError(f'Cannot play {card}, not in hand')