from flask import Flask, request, jsonify
from ninetynine.board import Board
from ninetynine.deck import Deck
from ninetynine.hand import Hand

app = Flask(__name__)

board = Board()
deck = Deck()
red_hand = Hand('red')
green_hand = Hand('green')

@app.route("/")
def show_gameboard():
    return board.to_text()

@app.route("/start", methods=['POST'])
def start():
    """Start the game"""
    content = request.get_json()
    return 'FOOBAR2k', 204

@app.route("/draw", methods=['POST'])
def draw():
    """Draw a card into players hand"""
    pass

@app.route("/play", methods=['GET'])
def play():
    """Play a card and claim a space"""
    color = request.args.get('color')
    num = int(request.args.get('num'))
    x = int(request.args.get('x'))
    y = int(request.args.get('y'))
    board.play(x, y, color, num)
    return board.to_text()

@app.route("/reset", methods=['POST'])
def reset():
    """Reset the game board and player hands"""
    pass