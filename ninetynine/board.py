from ninetynine.blank_board import blank_board
from ninetynine.illegal_move_error import IllegalMoveError

class Board:
    """Object to hold the state of the game board"""
    def __init__(self):
        self.spaces = {}
        for x, y, num in blank_board:
            self.spaces[(x, y)] = {
                'num': num,
                'color': None
            }

    def play(self, x, y, color, num):
        if (x, y) == (10, 1):
            raise IllegalMoveError("Illegal move - You cannot play on the blank space")
        space = self.spaces[(x, y)]
        is_num_legal = num <= space['num']
        is_empty = space['color'] == None
        if not is_num_legal:
            raise IllegalMoveError("Illegal move - Your card must be equal to or lower than the number of the space")
        if not is_empty:
            raise IllegalMoveError("Illegal move - You must play on an empty space")
        if is_num_legal and is_empty:
            self.spaces[(x, y)]['color'] = color

    
    def to_text(self):
        """Make a good representation for display on page as text here"""
        pass
        