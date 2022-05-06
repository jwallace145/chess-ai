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
    def __init__(self, color: Color, coordinates: Tuple[int, int]) -> None:
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
        if self.has_moved:
            if self.color == Color.BLACK:
                self.moves = [MOVE_DOWN_ONE]
            elif self.color == Color.WHITE:
                self.moves = [MOVE_UP_ONE]
        return super().get_possible_moves()
