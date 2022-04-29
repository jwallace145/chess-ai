from typing import Tuple

from src.constants import PieceEnum
from src.pieces.piece import Piece


class King(Piece):
    def __init__(self, color: str, coordinates: Tuple[int, int]) -> None:
        self.moves = [
            [(-1, 0)],
            [(1, 0)],
            [(0, -1)],
            [(0, 1)],
            [(1, -1)],
            [(1, 1)],
            [(-1, -1)],
            [(-1, 1)],
        ]
        super().__init__(PieceEnum.KING, color, coordinates, self.moves, self.moves)
