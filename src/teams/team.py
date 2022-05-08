from dataclasses import dataclass, field
from typing import Dict, Literal, Set, Tuple

from src.constants import Color, PieceName
from src.pieces.king import King
from src.pieces.piece import Piece


@dataclass
class Team:
    """Chess Team Base Class"""

    color: Literal[Color.BLACK, Color.WHITE]
    pieces: Dict[PieceName, Set[Piece]] = field(
        default_factory=lambda: {
            PieceName.PAWN: set(),
            PieceName.ROOK: set(),
            PieceName.KNIGHT: set(),
            PieceName.BISHOP: set(),
            PieceName.QUEEN: set(),
            PieceName.KING: set(),
        }
    )

    def remove_piece(self, piece: Piece) -> None:
        self.pieces[piece.name].remove(piece)

    def get_all_pieces(self) -> Set[Piece]:
        """Get all chess pieces on the same team.

        Returns:
            Set[Piece]: The set of chess pieces.
        """
        pieces = set()
        for pieces_set in self.pieces.values():
            for piece in pieces_set:
                pieces.add(piece)
        return pieces

    def get_king(self) -> King:
        """Get the king.

        Returns:
            King: The king piece.
        """
        king = self.pieces.get(PieceName.KING).pop()
        self.pieces.get(PieceName.KING).add(king)
        return king

    def get_piece(self, coordinates: Tuple[int, int]) -> Piece:
        """Get piece by its coordinates.

        Args:
            coordinates (Tuple[int, int]): The coordinates of the piece.

        Returns:
            Piece: The piece at given coordinates. If a piece does not exist at given coordinates, return None.
        """
        for piece in self.get_all_pieces():
            if piece.coordinates == coordinates:
                return piece

    def get_pieces(self, piece: PieceName) -> Set[Piece]:
        """Get all the pieces of same type (aka Pawns, Rooks, etc).

        Args:
            piece (PieceName): The type of piece.

        Returns:
            Set[Piece]: The set of chess pieces of the given type.
        """
        return self.pieces.get(piece)

    def set_pieces(self, pieces: Dict[PieceName, Set[Piece]]) -> None:
        """Set the pieces dictionary.

        Args:
            pieces (Dict[PieceName, Set[Piece]]): The pieces dictionary of all the chess pieces on a given team.
        """
        self.pieces = pieces

    def add_piece(self, piece: Piece) -> None:
        """Add a chess piece to the pieces dictionary.

        Args:
            piece (Piece): The chess piece.
        """
        self.pieces[piece.name].add(piece)

    def get_moves(self) -> Set[Tuple[Piece, Tuple[int, int]]]:
        """Get all the valid moves for the given team.

        Returns:
            Set[Tuple[int, int]]: The set of valid moves.
        """
        valid_moves = set()
        for piece in self.get_all_pieces():
            for move in piece.get_moves():
                valid_moves.add((piece, move))
        return valid_moves

    def get_valid_moves_except_king(self) -> Set[Tuple[int, int]]:
        """Get all the valid moves that can be made by the team except for the King.

        This method is helpful for determining if a friendly piece can block a check.

        Returns:
            Set[Tuple[int, int]]: The set of valid moves.
        """
        valid_moves_except_king = set()
        for piece in self.get_all_pieces():
            if not isinstance(piece, King):
                valid_moves_except_king.update(piece.get_valid_moves())
        return valid_moves_except_king

    def initialize(self) -> None:
        """Initialize the team in a standard chess configuration.

        This method is meant to be implemented by the Black and White subclasses
        since the standard chess configuration differs by team.
        """
        pass
