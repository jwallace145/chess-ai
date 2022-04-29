from dataclasses import dataclass, field
from typing import List, Set, Tuple

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
        if self.is_legal_move(dest):
            piece = self._pickup_piece(src)
            self._place_piece(piece, dest)

    def print_board(self) -> None:
        for row in range(NUM_OF_ROWS):
            print()
            for col in range(NUM_OF_COLS):
                piece = self._board[row][col] if self._board[row][col] else "--"
                print("| " + str(piece) + " |", end="")

    def _is_valid_coordinates(self, coordinates: Tuple[int, int]) -> bool:
        row, col = coordinates
        if 0 <= row < NUM_OF_ROWS and 0 <= col < NUM_OF_COLS:
            return True
        return False

    def _is_vacant(self, coordinates: Tuple[int, int]) -> bool:
        row, col = coordinates
        if self._board[row][col] is None:
            return True
        return False

    def is_legal_move(self, coordinates: Tuple[int, int]) -> bool:
        if self._is_valid_coordinates(coordinates) and self._is_vacant(coordinates):
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

    def get_valid_moves(self, coordinates: Tuple[int, int]) -> Set[Tuple[int, int]]:
        row, col = coordinates
        piece = self._get_piece(coordinates)

        valid_moves = []
        for direction in piece.moves:
            for move in direction:
                row_offset, col_offset = move
                new_row = row + row_offset
                new_col = col + col_offset
                new_coordinates = (new_row, new_col)
                if self._is_valid_coordinates(new_coordinates):
                    if self._is_vacant(new_coordinates):
                        valid_moves.append(new_coordinates)
                    elif self._is_capture(piece, new_coordinates):
                        valid_moves.append(new_coordinates)
                        break
                    else:
                        break
                else:
                    break
        return valid_moves
