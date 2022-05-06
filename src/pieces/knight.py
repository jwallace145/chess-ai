from typing import Tuple

from src.constants import Color, PieceEnum
from src.pieces.piece import Piece
from src.pieces.moves import (
    MOVE_UP_TWO_LEFT_ONE,
    MOVE_UP_TWO_RIGHT_ONE,
    MOVE_DOWN_TWO_LEFT_ONE,
    MOVE_DOWN_TWO_RIGHT_ONE,
    MOVE_LEFT_TWO_UP_ONE,
    MOVE_LEFT_TWO_DOWN_ONE,
    MOVE_RIGHT_TWO_UP_ONE,
    MOVE_RIGHT_TWO_DOWN_ONE,
)


class Knight(Piece):
    def __init__(self, color: Color, coordinates: Tuple[int, int]) -> None:
        self.moves = [
            MOVE_UP_TWO_LEFT_ONE,
            MOVE_UP_TWO_RIGHT_ONE,
            MOVE_DOWN_TWO_LEFT_ONE,
            MOVE_DOWN_TWO_RIGHT_ONE,
            MOVE_LEFT_TWO_UP_ONE,
            MOVE_LEFT_TWO_DOWN_ONE,
            MOVE_RIGHT_TWO_UP_ONE,
            MOVE_RIGHT_TWO_DOWN_ONE,
        ]
        self.captures = self.moves
        super().__init__(
            PieceEnum.KNIGHT, color, coordinates, self.moves, self.captures
        )
