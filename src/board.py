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
            self.place_piece(Pawn(Color.BLACK, (1, col)))
            self.place_piece(Pawn(Color.WHITE, (6, col)))

        # insert other pieces
        for col, piece in enumerate(
            [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        ):
            self.place_piece(piece(Color.BLACK, (0, col)))
            self.place_piece(piece(Color.WHITE, (7, col)))

    def place_piece(self, piece: Piece) -> None:
        if self.is_legal_move(piece.coordinates):
            row, col = piece.coordinates
            self._board[row][col] = piece

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
        piece = self._get_piece(coordinates)

        valid_moves = []
        for move in piece.get_moves():
            if self._is_vacant(move):
                valid_moves.append(move)

        for capture in piece.get_captures():
            if self._is_capture(piece, capture):
                valid_moves.append(capture)
        return valid_moves
