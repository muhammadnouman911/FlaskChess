
---

# FlaskChess ♟️

**FlaskChess** is a web-based chess application built using the Flask web framework and integrated with the Stockfish chess engine for powerful move analysis and gameplay.

## 🔧 Features

- ♟️ Play chess directly in your browser
- 🤖 Powered by Stockfish chess engine for move validation and AI opponent
- 🎨 Clean UI using Flask templates and static files
- ✅ Basic test script for board functionality

## 📁 Project Structure

```
FlaskChess/
│
├── flask_app.py         # Main Flask application
├── board_test.py        # Python script to test board logic
├── stockfish/           # Stockfish engine integration
├── templates/           # HTML templates for the front-end
├── static/              # CSS/JS files
├── README.md            # Project documentation
└── __pycache__/         # Python bytecode cache
```

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Flask
- Stockfish engine (included or needs to be downloaded separately)

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/FlaskChess.git
cd FlaskChess

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

### Run the Application

```bash
python flask_app.py
```

Then open your browser and go to:  
**http://127.0.0.1:5000**

## 🧠 Powered By

- [Flask](https://flask.palletsprojects.com/)
- [Stockfish Chess Engine](https://stockfishchess.org/)

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
