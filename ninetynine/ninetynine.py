from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def show_gameboard():
    return "This will show the gameboard"

@app.route("/start", methods=['POST'])
def start():
    """Start the game"""
    content = request.get_json()
    return 'FOOBAR2k', 204

@app.route("/draw", methods=['POST'])
def draw():
    """Draw a card into players hand"""
    pass

@app.route("/play", methods=['POST'])
def play():
    """Play a card and claim a space"""
    pass

@app.route("/reset", methods=['POST'])
def reset():
    """Reset the game board and player hands"""
    pass