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

    def check_if_won(self):
        """Checks if a given move won the game"""
        # Check spaces around you, if any are same color keep going that direction
        pass

    def to_text(self):
        """Make a good representation for display on page as text here"""
        text = ''
        # ys first
        for y in range(1, 11):
            # xs second
            text += '-' * 10 * 10 + '-'
            text += '\n' 
            for x in range(1, 11):
                space = self.spaces[(x, y)]
                color = space['color']
                num = self.equal_width_int_string(space['num'])
                text += f'| {num} {color} '
            text += '|\n'
        text += '-' * 10 * 10 + '-'
        print(text)
        return(text.replace('\n', '<br/>'))
    
    def equal_width_int_string(self, num):
        if num is None:
            return 'XX'
        s = str(num)
        if num < 10:
            s = '0' + s
        return s
        