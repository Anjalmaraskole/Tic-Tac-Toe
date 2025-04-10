# Tic-Tac-Toe
A simple, interactive Tic Tac Toe game built with Python Flask backend and HTML/CSS/JavaScript frontend.
This Tic Tac Toe application provides a sleek, responsive gaming experience with visual feedback and animations. The game features a clean user interface with a gradient background, animated elements, and celebratory effects when a player wins.

# **Tic Tac Toe Web Application**

A Python-based Tic Tac Toe game using Flask for the backend and HTML/CSS/JavaScript for the frontend. This system provides a fun, interactive way to play Tic Tac Toe with visual enhancements and smooth gameplay.

---

## **Tic Tac Toe Game System**

A comprehensive Python application for playing Tic Tac Toe in real-time. This system allows two players to compete on a responsive web-based interface while providing features like win detection, tie detection, and celebratory effects.

---

## 📋 **Features**

- **Interactive Game Board**: A responsive 3x3 grid dynamically updates as players take turns placing X's and O's.
- **Player Turn Tracking**: Displays the current player (X or O) at the top of the screen.
- **Win Detection**: Automatically detects winning combinations and announces the winner.
- **Animated Win Line**: A green line connects the winning cells to highlight the victory.
- **Confetti Celebration**: Colorful confetti launches from the bottom and sides of the screen when a player wins.
- **Tie Detection**: Identifies when the game ends in a draw and displays a tie notification.
- **Game Reset**: Allows players to start a new game at any time by clicking the "New Game" button.
- **Popup Notifications**: Displays popups for game outcomes (winner or tie).

---

## 🗂️ **Project Structure**

tic-tac-toe/
├── app.py # Flask application handling backend logic
├── templates/
│ └── index.html # Frontend UI with embedded CSS and JavaScript
└── README.md # Project documentation


### **File Descriptions**
- **`app.py`**: Handles backend logic, including game state management, move validation, win detection, and reset functionality.
- **`index.html`**: The frontend interface that includes dynamic cell creation, visual effects, and AJAX communication with the backend.

---

## 🔧 **Requirements**

To run this project, you’ll need:
- Python 3.6+
- Flask (Python web framework)
- A modern web browser (e.g., Chrome, Firefox)

---

## 📦 **Installation**

### 1. Clone this Repository
git clone https://github.com/yourusername/tic-tac-toe.git
cd tic-tac-toe


### 2. Create a Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

### 3. Install Dependencies
pip install flask

---

## 🚀 **Usage**

### Running the Application
1. Start the Flask server: python app.py
2. Open your web browser and navigate to: http://localhost:5000
   

### Playing the Game
1. The game starts with Player X's turn.
2. Click on any empty cell to place your mark (X or O).
3. Players alternate turns until one player gets three marks in a row (horizontally, vertically, or diagonally) or the board is full.
4. If a player wins:
- A green line connects the winning cells.
- Confetti launches from the bottom and sides of the screen.
- A popup announces "Winner: X" or "Winner: O."
5. If all cells are filled without a winner:
- A popup announces "It's a tie!"
6. To start a new game, click on "New Game," which resets the board.

---

## 📊 **Backend Logic**

The backend is implemented in Flask and manages:
- Game state using a dictionary of unique game IDs (`games`).
- Player turns and board updates through `/move/<game_id>` route.
- Win detection using predefined winning combinations in `check_win()`.
- Reset functionality through `/reset/<game_id>` route.

---

## 🎨 **Frontend Logic**

The frontend is built using HTML, CSS, and JavaScript:
- **Dynamic Grid Creation**: JavaScript dynamically generates cells for the grid on page load.
- **AJAX Communication**: Fetch API is used to send moves to the backend and update the board without reloading the page.
- **Visual Effects**:
- Animated win line calculated based on cell positions using CSS transformations.
- Confetti effects using `canvas-confetti` library for celebrations.
- Popups for displaying results like "Winner" or "Tie."

---

## 🔧 **Future Enhancements**

If further development is planned, consider adding:
1. Multiplayer functionality across devices.
2. AI opponent with adjustable difficulty levels.
3. Sound effects for moves and wins.
4. Customizable player names or symbols.
5. Game statistics tracking (e.g., win rates).

---

## 🤝 **Contributing**

Contributions are welcome! If you'd like to contribute:
1. Fork this repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to your branch (`git push origin feature-name`).
5. Submit a Pull Request.

---

## 📞 **Contact**

If you have any questions or suggestions, feel free to contact me at akulaanshulrao@gmail.com.

---

You can copy this directly into your `README.md` file in your GitHub repository! Let me know if you need further assistance! 😊





