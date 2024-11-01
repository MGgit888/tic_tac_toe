# README for Flask Tic Tac Toe Game

This project implements a simple Tic Tac Toe game using Flask for the backend logic and potentially a frontend framework (not included at this time) for the user interface. Though, if you want to use Postman you will see the game board pretty nicely.

Installation

    Ensure you have Python 3 and pip installed on your system.
    Clone or download this repository.
    Open a terminal in the project directory and run pip install flask.

Usage

    Run the Flask application using the command: python flask_ttt_app.py
    This will start the development server, typically accessible at http://127.0.0.1:5000/ in your web browser. The exact port can be changed by editing the flask_ttt_app.py (see example within)

    Once up and running you can connect to http://127.0.0.1:5000/get-board in your browser or in Postman

    You can make a move by accessing the make-move endpoint with the json of the index value you wish to replace with your X. Yes, that's right you can be either X or O as long as it's X.

    Once you make your move, the computer opponent will choose it's place for an O and it will be your turn again. 

API Endpoints:

    GET /get-board: Retrieves the current state of the game board in JSON format.
    POST /make-move: Makes a move on the board. Send a JSON object with the following key:
        index: The index of the cell on the board (1-9).
        example (from Postman)
        http://127.0.0.1:5000/make-move
            with json body as
            {"index": 3}
    POST /reset-board: Resets the game board to its initial state.

Frontend Integration:

This project provides a basic backend for a Tic Tac Toe game. I'm happy to take suggestions on how best to approach this.

# Code Structure

# The project consists of two main Python files:

    flask_ttt_app.py: This file implements the Flask application logic, handling API requests and managing the game state through the TicTacToeGame class.
    tic_tac_toe_logic.py: This file defines the core game logic, including board representation, move validation, win/tie checking, and a very basic random computer opponent.

# Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit pull requests. Here are some potential areas for improvement:

    Implement a user interface using HTML, CSS, and Javascript.
    Enhance the game logic with a more intelligent computer opponent (e.g., using minimax algorithm)
    Add features like player vs player mode.

# License

This project is licensed under the gnu general public license (gpl).