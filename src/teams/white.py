from dataclasses import dataclass, field
from typing import Dict, Set

from src.constants import Color, PieceEnum
from src.pieces.bishop import Bishop
from src.pieces.king import King
from src.pieces.knight import Knight
from src.pieces.pawn import Pawn
from src.pieces.piece import Piece
from src.pieces.queen import Queen
from src.pieces.rook import Rook
from src.teams.starting_coordinates import *
from src.teams.team import Team


@dataclass
class White(Team):

    color: Color = Color.WHITE
    pieces: Dict[PieceEnum, Set[Piece]] = field(
        default_factory=lambda: {
            PieceEnum.PAWN: set(
                [
                    Pawn(Color.WHITE, WHITE_PAWN_A2),
                    Pawn(Color.WHITE, WHITE_PAWN_B2),
                    Pawn(Color.WHITE, WHITE_PAWN_C2),
                    Pawn(Color.WHITE, WHITE_PAWN_D2),
                    Pawn(Color.WHITE, WHITE_PAWN_E2),
                    Pawn(Color.WHITE, WHITE_PAWN_F2),
                    Pawn(Color.WHITE, WHITE_PAWN_G2),
                    Pawn(Color.WHITE, WHITE_PAWN_H2),
                ]
            ),
            PieceEnum.ROOK: set(
                [
                    Rook(Color.WHITE, WHITE_ROOK_A1),
                    Rook(Color.WHITE, WHITE_ROOK_H1),
                ]
            ),
            PieceEnum.KNIGHT: set(
                [
                    Knight(Color.WHITE, WHITE_KNIGHT_B1),
                    Knight(Color.WHITE, WHITE_KNIGHT_G1),
                ]
            ),
            PieceEnum.BISHOP: set(
                [
                    Bishop(Color.WHITE, WHITE_BISHOP_C1),
                    Bishop(Color.WHITE, WHITE_BISHOP_F1),
                ]
            ),
            PieceEnum.QUEEN: set([Queen(Color.WHITE, WHITE_QUEEN_D1)]),
            PieceEnum.KING: set([King(Color.WHITE, WHITE_KING_E1)]),
        }
    )

    def __post_init__(self) -> None:
        super().__init__(self.color, self.pieces)
