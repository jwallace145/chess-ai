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
