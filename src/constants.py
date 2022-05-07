from enum import Enum

"""Chess Board Size"""
NUM_OF_ROWS = 8
NUM_OF_COLS = 8


class Color(Enum):
    """Chess Team Colors"""

    BLACK = "B"
    WHITE = "W"


class PieceEnum(Enum):
    """Chess Piece Name Enum"""

    PAWN = "P"
    ROOK = "R"
    BISHOP = "B"
    KNIGHT = "N"
    QUEEN = "Q"
    KING = "K"


class MenuOption(Enum):
    """Terminal Menu Options"""

    MOVE_A_PIECE = "move a piece"
    GET_VALID_MOVES = "get valid moves"


"""Chess Piece Values Dictionary"""
PIECE_VALUE = {
    PieceEnum.PAWN: 1,
    PieceEnum.ROOK: 5,
    PieceEnum.BISHOP: 3,
    PieceEnum.KNIGHT: 3,
    PieceEnum.QUEEN: 9,
    PieceEnum.KING: 1000,
}

"""Chess Board Columns Dictionary"""
COLUMNS = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}


"""Chess Board Piece Dictionary"""
PIECES = {
    "p": PieceEnum.PAWN,
    "r": PieceEnum.ROOK,
    "b": PieceEnum.BISHOP,
    "n": PieceEnum.KNIGHT,
    "q": PieceEnum.QUEEN,
    "k": PieceEnum.KING,
}
