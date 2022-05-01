from typing import Tuple

from src.constants import PieceEnum
from src.pieces.moves import (
    MOVE_DOWN,
    MOVE_DOWN_LEFT_DIAGONALLY,
    MOVE_DOWN_RIGHT_DIAGONALLY,
    MOVE_LEFT,
    MOVE_RIGHT,
    MOVE_UP,
    MOVE_UP_LEFT_DIAGONALLY,
    MOVE_UP_RIGHT_DIAGONALLY,
)
from src.pieces.piece import Piece


class Queen(Piece):
    def __init__(self, color: str, coordinates: Tuple[int, int]) -> None:
        self.moves = [
            MOVE_UP,
            MOVE_DOWN,
            MOVE_LEFT,
            MOVE_RIGHT,
            MOVE_UP_RIGHT_DIAGONALLY,
            MOVE_UP_LEFT_DIAGONALLY,
            MOVE_DOWN_RIGHT_DIAGONALLY,
            MOVE_DOWN_LEFT_DIAGONALLY,
        ]
        self.captures = self.moves
        super().__init__(PieceEnum.QUEEN, color, coordinates, self.moves, self.captures)
