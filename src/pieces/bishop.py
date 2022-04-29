from typing import Tuple

from src.constants import PieceEnum
from src.pieces.piece import Piece


class Bishop(Piece):
    def __init__(self, color: str, coordinates: Tuple[int, int]) -> None:
        super().__init__(PieceEnum.BISHOP, color, coordinates, [], [])
