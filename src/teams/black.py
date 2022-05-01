from src.constants import Color, PieceEnum
from src.pieces.bishop import Bishop
from src.pieces.king import King
from src.pieces.knight import Knight
from src.pieces.pawn import Pawn
from src.pieces.queen import Queen
from src.pieces.rook import Rook
from src.teams.team import Team


class Black(Team):
    def __init__(self) -> None:
        super().__init__(Color.BLACK)

    def initialize(self) -> None:
        self.pieces = {
            PieceEnum.PAWN: set(
                [
                    Pawn(Color.BLACK, (1, 0)),
                    Pawn(Color.BLACK, (1, 1)),
                    Pawn(Color.BLACK, (1, 2)),
                    Pawn(Color.BLACK, (1, 3)),
                    Pawn(Color.BLACK, (1, 4)),
                    Pawn(Color.BLACK, (1, 5)),
                    Pawn(Color.BLACK, (1, 6)),
                    Pawn(Color.BLACK, (1, 7)),
                ]
            ),
            PieceEnum.ROOK: set([Rook(Color.BLACK, (0, 0)), Rook(Color.BLACK, (0, 7))]),
            PieceEnum.KNIGHT: set(
                [Knight(Color.BLACK, (0, 1)), Knight(Color.BLACK, (0, 6))]
            ),
            PieceEnum.BISHOP: set(
                [Bishop(Color.BLACK, (0, 2)), Bishop(Color.BLACK, (0, 5))]
            ),
            PieceEnum.QUEEN: set([Queen(Color.BLACK, (0, 3))]),
            PieceEnum.KING: set([King(Color.BLACK, (0, 4))]),
        }
        self.set_pieces(self.pieces)
