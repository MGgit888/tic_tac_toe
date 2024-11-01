from flask import Flask, jsonify, request, session
from tic_tac_toe_logic import TicTacToeGame
import pickle

app = Flask(__name__)
app.secret_key = "your_secret_key"


def get_game() -> TicTacToeGame:
    if "game" not in session:
        session["game"] = pickle.dumps(TicTacToeGame())
    return pickle.loads(session["game"])


def save_game(game: TicTacToeGame):
    session["game"] = pickle.dumps(game)


@app.route("/get-board")
def board_api():
    game = get_game()
    return jsonify(game.get_board_json())


@app.route("/make-move", methods=["POST"])
def make_move():
    game = get_game()
    index = int(request.json.get("index"))
    result = game.make_move(index)
    save_game(game)
    return jsonify(result)


@app.route("/reset-board", methods=["POST"])
def reset_board():
    game = get_game()
    game.reset_board()
    save_game(game)
    return jsonify({"message": "Board has been reset", "board": game.get_board_json()})


if __name__ == "__main__":
    app.run(debug=True)
