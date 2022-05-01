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

COLUMNS = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}

PIECES = {
    "p": PieceEnum.PAWN,
    "r": PieceEnum.ROOK,
    "b": PieceEnum.BISHOP,
    "n": PieceEnum.KNIGHT,
    "q": PieceEnum.QUEEN,
    "k": PieceEnum.KING,
}
