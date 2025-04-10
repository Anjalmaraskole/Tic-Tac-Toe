# Tic-Tac-Toe
A simple, interactive Tic Tac Toe game built with Python Flask backend and HTML/CSS/JavaScript frontend.
This Tic Tac Toe application provides a sleek, responsive gaming experience with visual feedback and animations. The game features a clean user interface with a gradient background, animated elements, and celebratory effects when a player wins.

📋 Features
Interactive Game Board: A responsive 3x3 grid dynamically updates as players take turns placing X's and O's.

Player Turn Tracking: Displays the current player (X or O) at the top of the screen.

Win Detection: Automatically detects winning combinations and announces the winner.

Animated Win Line: A green line connects the winning cells to highlight the victory.

Confetti Celebration: Colorful confetti launches from the bottom and sides of the screen when a player wins.

Tie Detection: Identifies when the game ends in a draw and displays a tie notification.

Game Reset: Allows players to start a new game at any time by clicking the "New Game" button.

Popup Notifications: Displays popups for game outcomes (winner or tie).

🗂️ Project Structure
graphql
Copy
Edit
tic-tac-toe/
├── app.py                 # Flask application handling backend logic
├── templates/
│   └── index.html         # Frontend UI with embedded CSS and JavaScript
└── README.md              # Project documentation
File Descriptions
app.py: Handles backend logic, including game state management, move validation, win detection, and reset functionality.

index.html: The frontend interface that includes dynamic cell creation, visual effects, and AJAX communication with the backend.

🔧 Requirements
To run this project, you’ll need:

Python 3.6+

Flask (Python web framework)

A modern web browser (e.g., Chrome, Firefox)

📦 Installation
1. Clone this Repository
bash
Copy
Edit
git clone https://github.com/yourusername/tic-tac-toe.git
cd tic-tac-toe
2. Create a Virtual Environment (Optional but Recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install flask
🚀 Usage
Running the Application
Start the Flask server:

bash
Copy
Edit
python app.py
Then open your browser and go to:

arduino
Copy
Edit
http://localhost:5000
Playing the Game
The game starts with Player X's turn.

Click on any empty cell to place your mark (X or O).

Players alternate turns until one player gets three marks in a row (horizontally, vertically, or diagonally) or the board is full.

If a player wins:

A green line connects the winning cells.

Confetti launches from the screen edges.

A popup announces "Winner: X" or "Winner: O".

If it's a tie:

A popup announces "It's a tie!"

Click "New Game" to reset the board.

📊 Backend Logic
The backend is implemented in Flask and manages:

Game state using a dictionary of unique game IDs.

Player turns and board updates via /move/<game_id> route.

Win detection using predefined combinations in check_win().

Game reset via /reset/<game_id> route.

🎨 Frontend Logic
The frontend uses HTML, CSS, and JavaScript:

Dynamic Grid: JavaScript generates the game grid at runtime.

AJAX Communication: Fetch API sends moves to the backend and updates the UI without page reloads.

Visual Effects:

Animated win line using CSS transforms.

Confetti effects via canvas-confetti library.

Popup messages for wins and ties.

🔧 Future Enhancements
Planned or suggested improvements:

Multiplayer mode across devices.

AI opponent with difficulty levels.

Sound effects for interactions.

Player customization (names/symbols).

Game statistics (e.g., win history).

🤝 Contributing
Contributions are welcome!
To contribute:

Fork the repo

Create a feature branch:

bash
Copy
Edit
git checkout -b feature-name
Commit your changes:

bash
Copy
Edit
git commit -m 'Add feature'
Push to your branch:

bash
Copy
Edit
git push origin feature-name
Open a Pull Request

📞 Contact
If you have any questions or ideas, reach out at:
📧 [your-email@example.com]
