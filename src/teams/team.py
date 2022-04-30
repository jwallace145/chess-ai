from dataclasses import dataclass
from typing import Literal, Dict, Set, Tuple
from src.constants import Color, PieceEnum
from src.pieces.piece import Piece
from src.pieces.king import King


@dataclass
class Team:

    color: Literal[Color.BLACK, Color.WHITE]
    pieces: Dict[PieceEnum, Set[Piece]]

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
