from src.constants import Color, PieceEnum
from src.pieces.bishop import Bishop
from src.pieces.king import King
from src.pieces.knight import Knight
from src.pieces.pawn import Pawn
from src.pieces.queen import Queen
from src.pieces.rook import Rook
from src.teams.team import Team
from typing_extensions import Self


class White(Team):
    def __init__(self) -> None:
        super().__init__(Color.WHITE)

    def initialize(self) -> Self:
        self.pieces = {
            PieceEnum.PAWN: set(
                [
                    Pawn(Color.WHITE, (6, 0)),
                    Pawn(Color.WHITE, (6, 1)),
                    Pawn(Color.WHITE, (6, 2)),
                    Pawn(Color.WHITE, (6, 3)),
                    Pawn(Color.WHITE, (6, 4)),
                    Pawn(Color.WHITE, (6, 5)),
                    Pawn(Color.WHITE, (6, 6)),
                    Pawn(Color.WHITE, (6, 7)),
                ]
            ),
            PieceEnum.ROOK: set([Rook(Color.WHITE, (7, 0)), Rook(Color.WHITE, (7, 7))]),
            PieceEnum.KNIGHT: set(
                [Knight(Color.WHITE, (7, 1)), Knight(Color.WHITE, (7, 6))]
            ),
            PieceEnum.BISHOP: set(
                [Bishop(Color.WHITE, (7, 2)), Bishop(Color.WHITE, (7, 5))]
            ),
            PieceEnum.QUEEN: set([Queen(Color.WHITE, (7, 3))]),
            PieceEnum.KING: set([King(Color.WHITE, (7, 4))]),
        }
        self.set_pieces(self.pieces)
        return self
