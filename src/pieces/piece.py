from dataclasses import dataclass
from typing import List, Literal, Tuple

from src.constants import NUM_OF_COLS, NUM_OF_ROWS, PIECE_VALUE, Color, PieceEnum


@dataclass
class Piece:
    """Piece Base Class"""

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
    moves: List[List[Tuple[int, int]]]
    captures: List[List[Tuple[int, int]]]
    has_moved: bool = False

    def __post_init__(self) -> None:
        self.value = PIECE_VALUE[self.name]

    def get_possible_moves(self) -> List[List[Tuple[int, int]]]:
        """Get possible moves given the piece's current coordinates and move vectors.

        This method finds all the possible moves within the range of the board bounds.
        This method does not find all the valid moves of a piece considering the placement
        of friendly and enemy pieces.

        Returns:
            List[List[Tuple[int, int]]]: The list of possible move vectors given the piece's coordinates.
        """
        directions = []
        row, col = self.coordinates
        for direction in self.moves:
            moves = []
            for row_offset, col_offset in direction:
                new_row = row + row_offset
                new_col = col + col_offset
                if self._is_valid_coordinates((new_row, new_col)):
                    moves.append((new_row, new_col))
            directions.append(moves)
        return directions

    def get_possible_captures(self) -> List[List[Tuple[int, int]]]:
        """Get possible captures given the piece's current coordinates and capture vectors.

        This method is similar to Piece.get_possible_moves but performs the logic for the
        capture vectors. The move and capture vectors ONLY differ for Pawns.

        Returns:
            List[List[Tuple[int, int]]]: The list of possible capture vectors given the piece's coordinates.
        """
        directions = []
        row, col = self.coordinates
        for direction in self.captures:
            captures = []
            for row_offset, col_offset in direction:
                new_row = row + row_offset
                new_col = col + col_offset
                if self._is_valid_coordinates((new_row, new_col)):
                    captures.append((new_row, new_col))
            directions.append(captures)
        return directions

    @staticmethod
    def _is_valid_coordinates(coordinates: Tuple[int, int]) -> bool:
        """Determine if the given coordinates are within the board's bounds.

        Args:
            coordinates (Tuple[int, int]): The given coordinates

        Returns:
            bool: True if the coordinates are within the board's bounds. Otherwise, False.
        """
        row, col = coordinates
        if 0 <= row < NUM_OF_ROWS and 0 <= col < NUM_OF_COLS:
            return True
        return False

    def __eq__(self, o: object) -> bool:
        """Return whether piece object is equivalent to other object.

        Args:
            o (object): The other object.

        Returns:
            bool: True if the objects are equal. Otherwise, False.
        """
        if isinstance(o, Piece):
            if (
                o.color == self.color
                and o.name == self.name
                and o.coordinates == self.coordinates
            ):
                return True
        return False

    def __hash__(self) -> int:
        """Return hash of piece.

        Returns:
            int: The hash of piece.
        """
        return hash(
            str(self.color.value) + str(self.name.value) + str(self.coordinates)
        )

    def __str__(self) -> str:
        """Return the piece represented as a string.

        Returns:
            str: The string representation of the piece.
        """
        return f"{self.color.value}{self.name.value}"
