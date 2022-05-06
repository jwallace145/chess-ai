from typing import Tuple

from src.board import Board
from src.constants import COLUMNS, NUM_OF_COLS, NUM_OF_ROWS
from src.exceptions import (
    InvalidColumnUserInput,
    InvalidCoordinatesUserInput,
    InvalidRowUserInput,
)


def convert_coordinates(coordinates: str) -> Tuple[int, int]:
    """Convert coordinates of syntax e.g. e4 to row, col coordinates e.g. (4, 4).

    Args:
        coordinates (str): The coordinates in string format.

    Raises:
        InvalidCoordinatesUserInput: Raises InvalidCoordinatesUserInput if more than row, col is provided as coordinates.
        InvalidColumnUserInput: Raises InvalidColumnUserInput if given column in string format is not within range a - g.
        InvalidRowUserInput: Raises InvalidRowUserInput if given row isnt within range [1, 8].

    Returns:
        Tuple[int, int]: The coordinates in row, col format.
    """
    if len(coordinates) != 2:
        raise InvalidCoordinatesUserInput(coordinates)

    col, row = coordinates

    if col.lower() not in COLUMNS:
        raise InvalidColumnUserInput(col)

    if int(row) < 1 or int(row) > NUM_OF_ROWS:
        raise InvalidRowUserInput(row)

    col = COLUMNS[col.lower()]
    row = -1 * int(row) + NUM_OF_ROWS

    return (row, col)


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
