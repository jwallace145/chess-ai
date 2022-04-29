from typing import Tuple

from src.constants import NUM_OF_COLS, NUM_OF_ROWS, PieceEnum
from src.pieces.piece import Piece


class Rook(Piece):
    def __init__(self, color: str, coordinates: Tuple[int, int]) -> None:
        row, col = coordinates
        self.moves = set([(row, c) for c in range(NUM_OF_COLS)])  # move right
        self.moves.update(set([(row, -c) for c in range(NUM_OF_COLS)]))  # move left
        self.moves.update(set([(r, col) for r in range(NUM_OF_ROWS)]))  # move down
        self.moves.update(set([(-r, col) for r in range(NUM_OF_ROWS)]))  # move up
        self.captures = self.moves
        super().__init__(PieceEnum.ROOK, color, coordinates, self.moves, self.captures)
