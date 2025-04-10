# Tic-Tac-Toe
A simple, interactive Tic Tac Toe game built with Python Flask backend and HTML/CSS/JavaScript frontend.
This Tic Tac Toe application provides a sleek, responsive gaming experience with visual feedback and animations. The game features a clean user interface with a gradient background, animated elements, and celebratory effects when a player wins.
📋 Features

Interactive Game Board: Responsive 3x3 grid with hover effects and visual feedback

Player Turn Tracking: Clear indication of current player (X or O)

Win Detection: Automatic detection of winning combinations

Visual Win Indication: Animated line connecting the winning cells

Celebration Effects: Colorful confetti animation when a player wins

Tie Game Detection: Identifies when the game ends in a draw

Game Reset: Option to start a new game at any time

Result Notifications: Pop-up messages for game outcomes

🗂️ Project Structure

app.py: Flask application containing game logic and API endpoints

templates/index.html: HTML template with embedded CSS and JavaScript for the game interface

README.md: Project documentation and instructions

🔧 Requirements

Python 3.6+

Flask

Modern web browser with JavaScript enabled

📦 Installation

Clone this repository: git clone https://github.com/yourusername/tic-tac-toe.git

Install required packages: pip install flask

🚀 Usage
Running the Application

Navigate to the project directory

Run python app.py

Open a web browser and go to http://localhost:5000

Playing the Game

Click on any empty cell to make a move

The game alternates between X and O players

When a player wins or the game ties, a popup will appear

Click "New Game" to reset the board and start over

📊 Game State Management
The Flask backend manages game states using a dictionary with the following structure:

game_id: Unique identifier for each game session

board: List representing the 3x3 game board

current_player: Indicates whose turn it is (X or O)

winner: Stores the winning player, if any

🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

📞 Contact
If you have any questions or suggestions, please open an issue or contact [your-email@example.com].
