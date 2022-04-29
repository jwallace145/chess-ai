from dataclasses import dataclass
from typing import Literal, Set, Tuple

from src.constants import NUM_OF_COLS, NUM_OF_ROWS, Color, PieceEnum


@dataclass
class Piece:

    name: Literal[
        PieceEnum.PAWN,
        PieceEnum.ROOK,
        PieceEnum.BISHOP,
        PieceEnum.KNIGHT,
        PieceEnum.QUEEN,
        PieceEnum.KING,
    ]
    color: Literal[Color.BLACK, Color.WHITE]
    coordinates: Tuple[int, int]
    moves: Set[Tuple[int, int]]
    captures: Set[Tuple[int, int]]

    def _is_valid_coordinates(self, coordinates: Tuple[int, int]) -> bool:
        row, col = coordinates
        if 0 <= row < NUM_OF_ROWS and 0 <= col < NUM_OF_COLS:
            return True
        return False

    def get_moves(self) -> Set[Tuple[int, int]]:
        moves = []
        row, col = self.coordinates
        for row_offset, col_offset in self.moves:
            new_row = row + row_offset
            new_col = col + col_offset
            if self._is_valid_coordinates((new_row, new_col)):
                moves.append((new_row, new_col))
        return moves

    def get_captures(self) -> Set[Tuple[int, int]]:
        captures = []
        row, col = self.coordinates
        for row_offset, col_offset in self.captures:
            new_row = row + row_offset
            new_col = col + col_offset
            if self._is_valid_coordinates((new_row, new_col)):
                captures.append((new_row, new_col))
        return captures

    def __str__(self) -> str:
        return f"{self.color.value}{self.name.value}"
