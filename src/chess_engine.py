from dataclasses import dataclass, field
from typing import List, Set, Tuple

from src.board import Board
from src.constants import Color
from src.pieces.piece import Piece
from src.teams.black import Black
from src.teams.team import Team
from src.teams.white import White


@dataclass
class ChessEngine:
    """Chess Engine"""

    _board: Board = field(default_factory=Board)
    _black: Team = field(default_factory=Black)
    _white: Team = field(default_factory=White)

    def __post_init__(self) -> None:
        """Post initialization."""
        # set chess board with given black/white teams
        self._set_board()

        # calculate team moves to get valid moves for every piece
        self._calculate_team_moves(self._black)
        self._calculate_team_moves(self._white)

    def _set_board(self) -> None:
        """Set chess board with black and white pieces."""
        for team in [self._black, self._white]:
            for piece in team.get_all_pieces():
                self._board.put_piece(piece, piece.coordinates)

    def move(self, src: Tuple[int, int], dest: Tuple[int, int]) -> None:
        """Move piece from src to dest.

        Args:
            src (Tuple[int, int]): The src coordinates
            dest (Tuple[int, int]): The dest coordinates
        """
        piece = self._board._pickup_piece(coordinates=src)
        piece.coordinates = dest
        self._board.move_piece(piece, dest)
        self._calculate_team_moves(self._black)
        self._calculate_team_moves(self._white)

    def _calculate_team_moves(self, team: Team) -> None:
        """Calculate moves for given team (Black or White).

        Args:
            team (Team): The given chess team. Black or White.
        """
        for piece in team.get_all_pieces():
            moves = self._calculate_piece_moves(piece)
            piece.set_moves(moves)

    def _calculate_piece_moves(self, piece: Piece) -> Set[Tuple[int, int]]:
        """Calculate possible moves a piece can make.

        This method finds all possible moves for a given piece and ensures not
        moving into a check or checkmate position.

        Args:
            piece (Piece): The chess piece.

        Returns:
            Set[Tuple[int, int]]: The set of valid moves for the chess piece.
        """
        moves = set()
        for direction in piece.get_possible_moves():
            for move in direction:
                if self._board.is_vacant(move):
                    moves.add(move)
                else:
                    break

        captures = set()
        for direction in piece.get_possible_captures():
            for capture in direction:
                if self._board.is_capture(piece, capture):
                    captures.add(capture)
                    break
                if not self._board.is_vacant(capture):
                    break

        return moves.union(captures)

    def put_piece(self, team: Team, piece: Piece, dest: Tuple[int, int]) -> None:
        self._board.put_piece(piece, dest)
        team.add_piece(piece)

    def move_or_capture(self, team: Team, piece: Piece, dest: Tuple[int, int]) -> Piece:
        captured = None
        if self._board.is_vacant(dest):
            self._board._pickup_piece(piece)
            self._board.put_piece(piece, dest)
        elif self._board.is_capture(piece, dest):
            self._board._pickup_piece(piece)
            captured = self._board._pickup_piece(coordinates=dest)
            self._board.put_piece(piece, dest)
            team.remove_piece(captured)

        self._calculate_team_moves(self._black)
        self._calculate_team_moves(self._white)

        return captured

    def is_check(self, team: Team, enemy: Team) -> bool:
        """Determines if given team is in a check position.

        Args:
            team (Team): The given team.

        Returns:
            bool: True if given team is in a check position. Otherwise, False.
        """
        king_coordinates = team.get_king().coordinates
        for piece, move in enemy.get_moves():
            if move == king_coordinates:
                return True
        return False

    def is_checkmate(self, team: Team) -> bool:
        """Determines if the given team is in a checkmate position.

        Args:
            team (Team): The given chess team.

        Returns:
            bool: True if the given team is in a checkmate position. Otherwise, False.
        """
        return True

    def get_piece(self, coordinates: Tuple[int, int]) -> Piece:
        return self._board.get_piece(coordinates)
