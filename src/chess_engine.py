from dataclasses import dataclass, field
from typing import Set, Tuple

from src.board import Board
from src.pieces.piece import Piece
from src.teams.black import Black
from src.teams.team import Team
from src.teams.white import White


@dataclass
class ChessEngine:

    _black: Team = field(default_factory=Black)
    _white: Team = field(default_factory=White)
    _board: Board = field(default_factory=Board)

    def __post_init__(self) -> None:
        self._set_board()
        self._calculate_team_moves(self._black)
        self._calculate_team_moves(self._white)

    def _set_board(self) -> None:
        for piece in self._black.get_all_pieces().union(self._white.get_all_pieces()):
            self._board.put_piece(piece, piece.coordinates)

    def _calculate_team_moves(self, team: Team) -> None:
        for piece in team.get_all_pieces():
            moves = self._calculate_piece_moves(piece)
            piece.set_moves(moves)

    def _calculate_piece_moves(self, piece: Piece) -> Set[Tuple[int, int]]:
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

        moves = moves.union(captures)

        return moves

    def get_piece(self, coordinates: Tuple[int, int]) -> Piece:
        return self._board.get_piece(coordinates)
