from typing import Tuple

from src.constants import NUM_OF_COLS, NUM_OF_ROWS, PieceEnum
from src.pieces.piece import Piece


class Rook(Piece):
    def __init__(self, color: str, coordinates: Tuple[int, int]) -> None:
        row, col = coordinates
        self.moves = []
        self.moves.append([(row, c) for c in range(1, NUM_OF_COLS)])
        self.moves.append([(row, -c) for c in range(1, NUM_OF_COLS)])
        self.moves.append([(r, col) for r in range(1, NUM_OF_ROWS)])
        self.moves.append([(-r, col) for r in range(1, NUM_OF_ROWS)])
        self.captures = self.moves
        super().__init__(PieceEnum.ROOK, color, coordinates, self.moves, self.captures)
