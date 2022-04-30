from typing import Tuple

from src.constants import Color, PieceEnum
from src.pieces.piece import Piece
from typing import List


class Pawn(Piece):
    def __init__(self, color: str, coordinates: Tuple[int, int]) -> None:
        if color == Color.BLACK:
            self.moves = [[(1, 0), (2, 0)]]
            self.captures = [[(1, -1)], [(1, 1)]]
        elif color == Color.WHITE:
            self.moves = [[(-1, 0), (-2, 0)]]
            self.captures = [[(-1, 1)], [(-1, -1)]]
        super().__init__(PieceEnum.PAWN, color, coordinates, self.moves, self.captures)

    def get_possible_moves(self) -> List[List[Tuple[int, int]]]:
        row = self.coordinates[0]
        if self.color == Color.BLACK and row != 1:
            self.moves = [[(1, 0)]]
        elif self.color == Color.WHITE and row != 6:
            self.moves = [[(-1, 0)]]
        return super().get_possible_moves()
