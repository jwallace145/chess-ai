from typing import Tuple

from src.constants import Color, PieceName
from src.pieces.piece import Piece
from src.pieces.moves import (
    MOVE_UP_ONE,
    MOVE_DOWN_ONE,
    MOVE_LEFT_ONE,
    MOVE_RIGHT_ONE,
    MOVE_UP_RIGHT_DIAGONALLY_ONE,
    MOVE_UP_LEFT_DIAGONALLY_ONE,
    MOVE_DOWN_RIGHT_DIAGONALLY_ONE,
    MOVE_DOWN_LEFT_DIAGONALLY_ONE,
)


class King(Piece):
    def __init__(self, color: Color, coordinates: Tuple[int, int]) -> None:
        self.moves = [
            MOVE_UP_ONE,
            MOVE_DOWN_ONE,
            MOVE_LEFT_ONE,
            MOVE_RIGHT_ONE,
            MOVE_UP_RIGHT_DIAGONALLY_ONE,
            MOVE_UP_LEFT_DIAGONALLY_ONE,
            MOVE_DOWN_RIGHT_DIAGONALLY_ONE,
            MOVE_DOWN_LEFT_DIAGONALLY_ONE,
        ]
        self.captures = self.moves
        super().__init__(PieceName.KING, color, coordinates, self.moves, self.captures)
