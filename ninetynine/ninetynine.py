from flask import Flask

app = Flask(__name__)

@app.route("/")
def show_gameboard():
    return "This will show the gameboard"
