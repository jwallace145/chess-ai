from dataclasses import dataclass, field
from typing import List, Literal, Set, Tuple

from src.constants import NUM_OF_COLS, NUM_OF_ROWS, Color, PieceEnum
from src.exceptions import InvalidMove
from src.pieces.piece import Piece
from src.teams.black import Black
from src.teams.team import Team
from src.teams.white import White


@dataclass
class Board:

    _turn: Literal[Color.BLACK, Color.WHITE] = Color.WHITE
    _black: Team = Black()
    _white: Team = White()
    _board: List[List[str]] = field(
        default_factory=lambda: [
            [None for _ in range(NUM_OF_COLS)] for _ in range(NUM_OF_ROWS)
        ]
    )

    def __post_init__(self) -> None:
        pieces = self._black.get_all_pieces().union(self._white.get_all_pieces())
        for piece in pieces:
            self._place_piece(piece, piece.coordinates)

    def move_piece(self, src: Tuple[int, int], dest: Tuple[int, int]) -> None:
        """Move chess piece to valid destination.

        Args:
            src (Tuple[int, int]): The coordinates of the chess piece.
            dest (Tuple[int, int]): The coordinates of the desitination.

        Raises:
            InvalidMove: Raise an InvalidMove exception if the move is not valid.
        """
        if dest in self.get_valid_moves(src):
            piece = self._pickup_piece(src)
            self._place_piece(piece, dest)
            self._turn = Color.BLACK if self._turn == Color.WHITE else Color.WHITE
        else:
            raise InvalidMove(dest)

    def _is_vacant(self, coordinates: Tuple[int, int]) -> bool:
        """Determine if the given cell is vacant or occupied.

        Args:
            coordinates (Tuple[int, int]): The coordinates of the cell.

        Returns:
            bool: True if the cell is currently vacant. Otherwise, False.
        """
        row, col = coordinates
        if self._board[row][col] is None:
            return True
        return False

    def _is_capture(self, piece: Piece, coordinates: Tuple[int, int]) -> bool:
        """Determine if moving the piece to the given destination cell is an enemy capture.

        Args:
            piece (Piece): The given chess piece.
            coordinates (Tuple[int, int]): The destination coordinates of possible enemy capture.

        Returns:
            bool: True if moving the given piece to the destination coordinates captures an enemy piece. Otherwise, False
        """
        enemy = self._get_piece(coordinates)
        if enemy and enemy.color != piece.color:
            return True
        return False

    def _get_piece(self, coordinates: Tuple[int, int]) -> Piece:
        """Get the chess piece at the given coordinates. Do not remove chess piece.

        Args:
            coordinates (Tuple[int, int]): The coordinates of the chess piece.

        Returns:
            Piece: The chess piece at given coordinates. If no chess piece exists at
                   the given coordinates return None.
        """
        row, col = coordinates
        return self._board[row][col]

    def _pickup_piece(self, coordinates: Tuple[int, int]) -> Piece:
        """Pick up and remove chess piece from given coordinates and return the chess piece.

        Args:
            coordinates (Tuple[int, int]): The coordinates of the chess piece.

        Returns:
            Piece: The chess piece at the given coordinates.
        """
        row, col = coordinates
        piece = self._board[row][col]
        self._board[row][col] = None
        return piece

    def _place_piece(self, piece: Piece, coordinates: Tuple[int, int]) -> None:
        """Place chess piece at the given coordinates.

        Args:
            piece (Piece): The chess piece.
            coordinates (Tuple[int, int]): The desired coordinates.
        """
        piece.coordinates = coordinates
        row, col = coordinates
        self._board[row][col] = piece

    def find_piece(self, piece: PieceEnum, dest_coordinates: Tuple[int, int]) -> Piece:
        """Find chess piece given the type of chess piece and destination coordinates.

        This method is helpful for finding the desired chess piece given a move in the
        syntax "P E4". This means move current team Pawn to square E4 (4,4).

        Args:
            piece (PieceEnum): The type of chess piece
            dest_coordinates (Tuple[int, int]): The destination coordinates of the given chess piece.

        Raises:
            InvalidMove: Raises an InvalidMove exception if none of the current team pieces can move to the
                         given destination square.

        Returns:
            Piece: The chess piece that can make to the given destination square.
        """
        if self._turn == Color.BLACK:
            pieces = self._black.get_pieces(piece)
        else:
            pieces = self._white.get_pieces(piece)

        possible_pieces = []
        for piece in pieces:
            if dest_coordinates in self.get_valid_moves(piece.coordinates):
                possible_pieces.append(piece)

        if len(possible_pieces) == 0:
            raise InvalidMove(dest_coordinates)
        elif len(possible_pieces) == 1:
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

    def is_check(self) -> bool:
        """Determines if current team is in a check position.

        Returns:
            bool: True if current team is in a check position. Otherwise, False.
        """
        if self._turn == Color.BLACK:
            king = self._black.get_king()
            enemy_pieces = self._white.get_all_pieces()
        else:
            king = self._white.get_king()
            enemy_pieces = self._black.get_all_pieces()

        enemy_valid_moves = set()
        for enemy in enemy_pieces:
            enemy_valid_moves.update(self.get_valid_moves(enemy.coordinates))

        if king.coordinates in enemy_valid_moves:
            return True
        return False

    def is_checkmate(self) -> bool:
        """Determines if current team is in a checkmate position.

        Returns:
            bool: True if current team is in a checkmate position. Otherwise, False.
        """
        if self._turn == Color.BLACK:
            king = self._black.get_king()
            enemy_pieces = self._white.get_all_pieces()
        else:
            king = self._white.get_king()
            enemy_pieces = self._black.get_all_pieces()

        king_moves = self.get_valid_moves(king.coordinates)

        enemy_valid_moves = set()
        for enemy in enemy_pieces:
            enemy_valid_moves.update(self.get_valid_moves(enemy.coordinates))

        for move in king_moves:
            if move not in enemy_valid_moves:
                return False
        return True
