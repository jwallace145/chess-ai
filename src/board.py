from dataclasses import dataclass, field
from typing import List, Literal, Set, Tuple

from src.constants import NUM_OF_COLS, NUM_OF_ROWS, Color
from src.pieces.bishop import Bishop
from src.pieces.king import King
from src.pieces.knight import Knight
from src.pieces.pawn import Pawn
from src.pieces.piece import Piece
from src.pieces.queen import Queen
from src.pieces.rook import Rook


@dataclass
class Board:

    _color: Literal[Color.BLACK, Color.WHITE] = Color.WHITE
    _board: List[List[str]] = field(
        default_factory=lambda: [
            [None for _ in range(NUM_OF_COLS)] for _ in range(NUM_OF_ROWS)
        ]
    )

    def __post_init__(self) -> None:
        # insert pawns
        for col in range(NUM_OF_COLS):
            self._place_piece(Pawn(Color.BLACK, (1, col)), (1, col))
            self._place_piece(Pawn(Color.WHITE, (6, col)), (6, col))

        # insert other pieces
        for col, piece in enumerate(
            [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        ):
            self._place_piece(piece(Color.BLACK, (0, col)), (0, col))
            self._place_piece(piece(Color.WHITE, (7, col)), (7, col))

    def move_piece(self, src: Tuple[int, int], dest: Tuple[int, int]) -> None:
        if dest in self.get_valid_moves(src):
            piece = self._pickup_piece(src)
            self._place_piece(piece, dest)

    def print_board(self) -> None:
        for row in range(NUM_OF_ROWS):
            print()
            for col in range(NUM_OF_COLS):
                piece = self._board[row][col] if self._board[row][col] else "--"
                print("| " + str(piece) + " |", end="")

    def _is_vacant(self, coordinates: Tuple[int, int]) -> bool:
        row, col = coordinates
        if self._board[row][col] is None:
            return True
        return False

    def _is_capture(self, piece: Piece, coordinates: Tuple[int, int]) -> bool:
        enemy = self._get_piece(coordinates)
        if enemy and enemy.color != piece.color:
            return True
        return False

    def _get_piece(self, coordinates: Tuple[int, int]) -> Piece:
        row, col = coordinates
        return self._board[row][col]

    def _pickup_piece(self, coordinates: Tuple[int, int]) -> Piece:
        row, col = coordinates
        piece = self._board[row][col]
        self._board[row][col] = None
        return piece

    def _place_piece(self, piece: Piece, coordinates: Tuple[int, int]) -> None:
        piece.coordinates = coordinates
        row, col = coordinates
        self._board[row][col] = piece

    def find_piece_coordinates(
        self, piece: str, dest_coordinates: Tuple[int, int]
    ) -> List[Tuple[int, int]]:
        possible_pieces = []
        for row in range(NUM_OF_ROWS):
            for col in range(NUM_OF_COLS):
                if (
                    not self._is_vacant((row, col))
                    and str(self._get_piece((row, col))) == piece
                    and dest_coordinates in self.get_valid_moves((row, col))
                ):
                    possible_pieces.append((row, col))

        if len(possible_pieces) == 0:
            print("NO PIECES FOUND")
            return
        elif len(possible_pieces) == 1:
            print("A PIECE FOUND")
            return possible_pieces[0]
        else:
            print("MULTIPLE PIECES FOUND NOT GOOD")
            return possible_pieces[0]

    def get_valid_moves(self, coordinates: Tuple[int, int]) -> Set[Tuple[int, int]]:
        """Get the valid moves of a piece.

        This method finds all the valid moves of a piece given its current coordinates. This
        method accounts for the location of friendly and enemy pieces for moves and captures.

        Args:
            coordinates (Tuple[int, int]): The coordinates of the piece.

        Returns:
            Set[Tuple[int, int]]: The set of valid coordinates the piece can move to.
        """
        piece = self._get_piece(coordinates)

        valid_moves = set()
        for direction in piece.get_possible_moves():
            for move in direction:
                if self._is_vacant(move):
                    valid_moves.add(move)
                else:
                    break

        valid_captures = set()
        for direction in piece.get_possible_captures():
            for move in direction:
                if not self._is_vacant(move) and self._is_capture(piece, move):
                    valid_captures.add(move)
                    break

        # return set of valid moves and valid captures
        return valid_moves.union(valid_captures)
