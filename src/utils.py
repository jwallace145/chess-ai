from src.board import Board
from src.constants import NUM_OF_COLS, NUM_OF_ROWS


def print_board(board: Board) -> None:
    """Print current chess board.

    Args:
        board (Board): The chess board.
    """
    print(f"Current turn: {board._current_team.color.name}")
    for row in range(NUM_OF_ROWS):
        print()
        for col in range(NUM_OF_COLS):
            piece = board._board[row][col] if board._board[row][col] else "--"
            print("| " + str(piece) + " |", end="")
