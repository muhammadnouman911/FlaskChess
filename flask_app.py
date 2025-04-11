from flask import Flask, render_template
import chess.engine
import os

# Initialize Flask app
app = Flask(__name__)

# Path to Stockfish binary (update with your actual path)
STOCKFISH_PATH = r"C:\Users\Aryan khan\OneDrive\Desktop\AI-FOR-CHESS-main\FlaskChess\stockfish\stockfish-windows-x86-64-avx2.exe"

# Ensure the Stockfish binary exists
if not os.path.exists(STOCKFISH_PATH):
    raise FileNotFoundError(f"Stockfish binary not found at {STOCKFISH_PATH}")


@app.route('/')
def index():
    """Render the index page."""
    return render_template("index.html")


@app.route('/move/<int:depth>/<path:fen>/')
def get_move(depth, fen):
    """Calculate the best move for a given FEN and depth using Stockfish."""
    try:
        print(f"Depth: {depth}")
        print("Calculating move...")
        
        # Initialize Stockfish engine
        with chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH) as engine:
            # Set up the board with the provided FEN
            board = chess.Board(fen)

            # Get the best move
            result = engine.play(board, chess.engine.Limit(depth=depth))
            move = result.move

            print("Move found!", move)
            return str(move)
    except Exception as e:
        print(f"Error: {e}")
        return str(e), 500


@app.route('/test/<string:tester>')
def test_get(tester):
    """Simple test route to echo the input."""
    return tester


if __name__ == "__main__":
    # Run the Flask app
    app.run(host="0.0.0.0", port=7000, debug=True)
