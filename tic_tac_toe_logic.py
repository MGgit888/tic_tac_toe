# tic_tac_toe_logic.py
import random
from typing import List, Dict

class TicTacToeGame:
    """Represents a Tic Tac Toe game."""
    def __init__(self):
        """Initializes a new game of Tic Tac Toe."""
        self.reset_board()

    def reset_board(self):
        """Resets the game board and sets the current player to X."""
        self.current_board: List[str] = [str(i) for i in range(1, 10)]
        self.current_player = "X"

    def get_board_json(self) -> Dict[str, str]:
        """Returns the current state of the game board as a JSON dictionary."""
        return {
            "row1": "".join(self.current_board[0:3]),
            "row2": "".join(self.current_board[3:6]),
            "row3": "".join(self.current_board[6:9]),
        }

    def make_move(self, index: int) -> Dict[str, str]:
        """Makes a move on the game board at the given index.

        Args:
            index: The index of the cell to play on (1-9).

        Returns:
            A dictionary containing the updated game state or an error message
            if the move is invalid.
        """
        idx = index - 1
        if idx < 0 or idx >= len(self.current_board) or self.current_board[idx] in ["X", "O"]:
            return {"error": "Invalid move"}

        self.current_board[idx] = self.current_player

        # Check if there is a winner or a tie
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

        # Check if there is a winner or tie after the computer move
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
        """Switches the current player."""
        self.current_player = "O" if self.current_player == "X" else "X"

    def computer_move(self):
        """Picks a random available place to make the computer move."""
        empty_indices = [i for i, x in enumerate(self.current_board) if x not in ["X", "O"]]
        if empty_indices:
            comp_idx = random.choice(empty_indices)
            self.current_board[comp_idx] = self.current_player

    def check_winner(self, player: str) -> bool:
        """Checks if the given player has a winning combination on the board.

        Args:
            player: The player to check for a win.

        Returns:
            True if the player has a winning combination, False otherwise.
        """
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
