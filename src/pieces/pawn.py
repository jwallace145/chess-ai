from typing import List, Tuple

from src.constants import Color, PieceEnum
from src.pieces.moves import (
    MOVE_DOWN_LEFT_DIAGONALLY_ONE,
    MOVE_DOWN_ONE,
    MOVE_DOWN_RIGHT_DIAGONALLY_ONE,
    MOVE_DOWN_TWO,
    MOVE_UP_LEFT_DIAGONALLY_ONE,
    MOVE_UP_ONE,
    MOVE_UP_RIGHT_DIAGONALLY_ONE,
    MOVE_UP_TWO,
)
from src.pieces.piece import Piece


class Pawn(Piece):
    def __init__(self, color: str, coordinates: Tuple[int, int]) -> None:
        if color == Color.BLACK:
            self.moves = [MOVE_DOWN_ONE, MOVE_DOWN_TWO]
            self.captures = [
                MOVE_DOWN_RIGHT_DIAGONALLY_ONE,
                MOVE_DOWN_LEFT_DIAGONALLY_ONE,
            ]
        elif color == Color.WHITE:
            self.moves = [MOVE_UP_ONE, MOVE_UP_TWO]
            self.captures = [
                MOVE_UP_RIGHT_DIAGONALLY_ONE,
                MOVE_UP_LEFT_DIAGONALLY_ONE,
            ]
        super().__init__(PieceEnum.PAWN, color, coordinates, self.moves, self.captures)

    def get_possible_moves(self) -> List[List[Tuple[int, int]]]:
        row = self.coordinates[0]
        if self.color == Color.BLACK and row != 1:
            self.moves = [[(1, 0)]]
        elif self.color == Color.WHITE and row != 6:
            self.moves = [[(-1, 0)]]
        return super().get_possible_moves()
