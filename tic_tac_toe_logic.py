# tic_tac_toe.py
import random
from typing import List, Dict

class TicTacToeGame:
    def __init__(self):
        self.reset_board()

    def reset_board(self):
        self.current_board: List[str] = [str(i) for i in range(1, 10)]
        self.current_player = "X"

    def get_board_json(self) -> Dict[str, str]:
        return {
            "row1": "".join(self.current_board[0:3]),
            "row2": "".join(self.current_board[3:6]),
            "row3": "".join(self.current_board[6:9]),
        }

    def make_move(self, index: int) -> Dict[str, str]:
        idx = index - 1
        if idx < 0 or idx >= len(self.current_board) or self.current_board[idx] in ["X", "O"]:
            return {"error": "Invalid move"}

        self.current_board[idx] = self.current_player

        if self.check_winner(self.current_player):
            response = {
                "message": f"{self.current_player} wins!",
                "board": self.get_board_json(),
            }
            self.reset_board()
            return response
        
        if self.is_tie():
            response = {
                "message": "It's a tie!",
                "board": self.get_board_json(),
            }
            self.reset_board()
            return response

        self.switch_player()
        self.computer_move()

        if self.check_winner(self.current_player):
            response = {
                "message": f"{self.current_player} wins!",
                "board": self.get_board_json(),
            }
            self.reset_board()
            return response
        
        if self.is_tie():
            response = {
                "message": "It's a tie!",
                "board": self.get_board_json(),
            }
            self.reset_board()
            return response

        self.switch_player()
        return self.get_board_json()

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def computer_move(self):
        empty_indices = [i for i, x in enumerate(self.current_board) if x not in ["X", "O"]]
        if empty_indices:
            comp_idx = random.choice(empty_indices)
            self.current_board[comp_idx] = self.current_player

    def check_winner(self, player: str) -> bool:
        win_conditions = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),  # Horizontal
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),  # Vertical
            (0, 4, 8),
            (2, 4, 6),  # Diagonal
        ]
        for cond in win_conditions:
            if self.current_board[cond[0]] == self.current_board[cond[1]] == self.current_board[cond[2]] == player:
                return True
        return False
    
    def is_tie(self) -> bool:
        """Check if the board is full and there is no winner."""
        return all(x in ["X", "O"] for x in self.current_board)
