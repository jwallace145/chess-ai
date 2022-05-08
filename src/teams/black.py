from dataclasses import dataclass, field
from typing import Dict, Set

from src.constants import Color, PieceName
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
class Black(Team):

    color: Color = Color.BLACK
    pieces: Dict[PieceName, Set[Piece]] = field(
        default_factory=lambda: {
            PieceName.PAWN: set(
                [
                    Pawn(Color.BLACK, BLACK_PAWN_A7),
                    Pawn(Color.BLACK, BLACK_PAWN_B7),
                    Pawn(Color.BLACK, BLACK_PAWN_C7),
                    Pawn(Color.BLACK, BLACK_PAWN_D7),
                    Pawn(Color.BLACK, BLACK_PAWN_E7),
                    Pawn(Color.BLACK, BLACK_PAWN_F7),
                    Pawn(Color.BLACK, BLACK_PAWN_G7),
                    Pawn(Color.BLACK, BLACK_PAWN_H7),
                ]
            ),
            PieceName.ROOK: set(
                [Rook(Color.BLACK, BLACK_ROOK_A8), Rook(Color.BLACK, BLACK_ROOK_H8)]
            ),
            PieceName.KNIGHT: set(
                [
                    Knight(Color.BLACK, BLACK_KNIGHT_B8),
                    Knight(Color.BLACK, BLACK_KNIGHT_G8),
                ]
            ),
            PieceName.BISHOP: set(
                [
                    Bishop(Color.BLACK, BLACK_BISHOP_C8),
                    Bishop(Color.BLACK, BLACK_BISHOP_F8),
                ]
            ),
            PieceName.QUEEN: set([Queen(Color.BLACK, BLACK_QUEEN_D8)]),
            PieceName.KING: set([King(Color.BLACK, BLACK_KING_E8)]),
        }
    )

    def __post_init__(self) -> None:
        super().__init__(self.color, self.pieces)
