from enum import Enum

NUM_OF_ROWS = 8
NUM_OF_COLS = 8


class Color(Enum):
    BLACK = "B"
    WHITE = "W"


class PieceEnum(Enum):
    PAWN = "P"
    ROOK = "R"
    BISHOP = "B"
    KNIGHT = "N"
    QUEEN = "Q"
    KING = "K"


PIECE_VALUE = {
    PieceEnum.PAWN: 1,
    PieceEnum.ROOK: 5,
    PieceEnum.BISHOP: 3,
    PieceEnum.KNIGHT: 3,
    PieceEnum.QUEEN: 9,
    PieceEnum.KING: 1000,
}
