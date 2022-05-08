from typing import Tuple

from src.constants import Color, PieceName
from src.pieces.piece import Piece
from src.pieces.moves import (
    MOVE_UP,
    MOVE_DOWN,
    MOVE_LEFT,
    MOVE_RIGHT,
)


class Rook(Piece):
    def __init__(self, color: Color, coordinates: Tuple[int, int]) -> None:
        self.moves = [MOVE_UP, MOVE_DOWN, MOVE_LEFT, MOVE_RIGHT]
        self.captures = self.moves
        super().__init__(PieceName.ROOK, color, coordinates, self.moves, self.captures)
