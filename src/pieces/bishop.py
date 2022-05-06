from typing import Tuple

from src.constants import PieceEnum, Color
from src.pieces.piece import Piece
from src.pieces.moves import (
    MOVE_UP_RIGHT_DIAGONALLY,
    MOVE_UP_LEFT_DIAGONALLY,
    MOVE_DOWN_RIGHT_DIAGONALLY,
    MOVE_DOWN_LEFT_DIAGONALLY,
)


class Bishop(Piece):
    def __init__(self, color: Color, coordinates: Tuple[int, int]) -> None:
        self.moves = [
            MOVE_UP_RIGHT_DIAGONALLY,
            MOVE_UP_LEFT_DIAGONALLY,
            MOVE_DOWN_RIGHT_DIAGONALLY,
            MOVE_DOWN_LEFT_DIAGONALLY,
        ]
        self.captures = self.moves
        super().__init__(
            PieceEnum.BISHOP, color, coordinates, self.moves, self.captures
        )
