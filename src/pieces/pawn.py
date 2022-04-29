from typing import Tuple

from src.constants import Color, PieceEnum
from src.pieces.piece import Piece


class Pawn(Piece):
    def __init__(self, color: str, coordinates: Tuple[int, int]) -> None:
        if color == Color.BLACK:
            self.moves = [(1, 0)]
            self.captures = [(1, -1), (1, 1)]
        elif color == Color.WHITE:
            self.moves = [(-1, 0)]
            self.captures = [(-1, 1), (-1, -1)]
        super().__init__(PieceEnum.PAWN, color, coordinates, self.moves, self.captures)
