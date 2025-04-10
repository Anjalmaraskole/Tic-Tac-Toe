
from flask import Flask, jsonify, request, render_template
import random

app = Flask(__name__)
games = {}

class TicTacToe:
    def __init__(self):
        self.board = [""] * 9
        self.current_player = "X"
        self.winner = None

    def make_move(self, position):
        if self.board[position] == "" and not self.winner:
            self.board[position] = self.current_player
            if self.check_win():
                self.winner = self.current_player
            self.current_player = "O" if self.current_player == "X" else "X"
            return True
        return False

    def check_win(self):
        win_combinations = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8],  [0,4,8], [2,4,6]]
        for combo in win_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return True
        return False

@app.route('/')
def index():
    game_id = str(random.randint(1000,9999))
    games[game_id] = TicTacToe()
    return render_template('index.html', game_id=game_id)

@app.route('/move/<game_id>', methods=['POST'])
def make_move(game_id):
    game = games.get(game_id)
    if not game:
        return jsonify({"error": "Game not found"}), 404
    data = request.json
    position = data.get('position')
    if game.make_move(position):
        return jsonify({
            "board": game.board,
            "current_player": game.current_player,
            "winner": game.winner
        })
    return jsonify({"error": "Invalid move"}), 400

@app.route('/reset/<game_id>', methods=['POST'])
def reset_game(game_id):
    if game_id in games:
        games[game_id] = TicTacToe()  
        return jsonify({
            "board": games[game_id].board,
            "current_player": games[game_id].current_player,
            "winner": None
        })
    return jsonify({"error": "Game not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)