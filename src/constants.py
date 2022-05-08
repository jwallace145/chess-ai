from enum import Enum

"""Chess Board Size"""
NUM_OF_ROWS = 8
NUM_OF_COLS = 8


class Color(Enum):
    """Chess Team Colors"""

    BLACK = "B"
    WHITE = "W"


class PieceName(Enum):
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
    PieceName.PAWN: 1,
    PieceName.ROOK: 5,
    PieceName.BISHOP: 3,
    PieceName.KNIGHT: 3,
    PieceName.QUEEN: 9,
    PieceName.KING: 1000,
}

"""Chess Board Columns Dictionary"""
COLUMNS = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}


"""Chess Board Piece Dictionary"""
PIECES = {
    "p": PieceName.PAWN,
    "r": PieceName.ROOK,
    "b": PieceName.BISHOP,
    "n": PieceName.KNIGHT,
    "q": PieceName.QUEEN,
    "k": PieceName.KING,
}
