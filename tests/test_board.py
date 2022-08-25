from ninetynine.board import Board
from ninetynine.illegal_move_error import IllegalMoveError

def test_can_play_legal_move():
    board = Board()
    board.play(2, 4, 'red', 53) # Lower than space value
    board.play(1, 1, 'blue', 73) # Equal to space value
    assert board.spaces[(2, 4)]['color'] == 'red'
    assert board.spaces[(1, 1)]['color'] == 'blue'

def test_cannot_play_blank_space():
    board = Board()
    try:
        board.play(10, 1, 'red', 0)
    except IllegalMoveError:
        pass
    assert board.spaces[(10, 1)]['color'] is None

def test_cannot_play_invalid_number():
    board = Board()
    try:
        board.play(1, 1, 'red', 99)
    except IllegalMoveError:
        pass
    assert board.spaces[(1, 1)]['color'] is None