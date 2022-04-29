from typing import Tuple

from src.constants import PieceEnum
from src.pieces.piece import Piece


class Knight(Piece):
    def __init__(self, color: str, coordinates: Tuple[int, int]) -> None:
        self.moves = [
            [(-2, -1)],
            [(-2, 1)],
            [(-1, -2)],
            [(-1, 2)],
            [(1, -2)],
            [(1, 2)],
            [(2, -1)],
            [(2, 1)],
        ]
        super().__init__(PieceEnum.KNIGHT, color, coordinates, self.moves, self.moves)
