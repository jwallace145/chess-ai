from dataclasses import dataclass, field
from typing import Dict, Literal, Set

from src.constants import Color, PieceEnum
from src.pieces.king import King
from src.pieces.piece import Piece


@dataclass
class Team:
    """Chess Team Base Class"""

    color: Literal[Color.BLACK, Color.WHITE]
    pieces: Dict[PieceEnum, Set[Piece]] = field(
        default_factory=lambda: {
            PieceEnum.PAWN: set(),
            PieceEnum.ROOK: set(),
            PieceEnum.KNIGHT: set(),
            PieceEnum.BISHOP: set(),
            PieceEnum.QUEEN: set(),
            PieceEnum.KING: set(),
        }
    )

    def get_all_pieces(self) -> Set[Piece]:
        pieces = set()
        for pieces_set in self.pieces.values():
            for piece in pieces_set:
                pieces.add(piece)
        return pieces

    def get_king(self) -> King:
        king = self.pieces.get(PieceEnum.KING).pop()
        self.pieces.get(PieceEnum.KING).add(king)
        return king

    def get_pieces(self, piece: PieceEnum) -> Set[Piece]:
        return self.pieces.get(piece)

    def set_pieces(self, pieces: Dict[PieceEnum, Set[Piece]]) -> None:
        self.pieces = pieces

    def add_piece(self, piece_enum: PieceEnum, piece: Piece) -> None:
        self.pieces.get(piece_enum).add(piece)

    def initialize(self) -> None:
        pass
