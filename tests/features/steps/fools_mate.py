from unittest.mock import NonCallableMagicMock

from behave import *
from src.board import Board
from src.chess_engine import ChessEngine
from src.teams.black import Black
from src.teams.white import White

FOOLS_MATE_MOVES = [
    ((6, 5), (5, 5)),
    ((1, 4), (3, 4)),
    ((6, 6), (4, 6)),
    ((0, 3), (4, 7)),
]


@given("a chess board and white and black teams")
def initialize_board_and_teams(context) -> None:
    """Initialize chess game (board, white team, black team).

    Args:
        context: The given context of the step.
    """
    context.board = Board()
    context.white = White()
    context.black = Black()
    context.chess_engine = ChessEngine(
        _board=context.board, _black=context.black, _white=context.white
    )


@when("we set the chess board in standard position")
def initialize_standard_game(context) -> None:
    """Initialize a standard game of chess.

    Args:
        context: The given context of the step.
    """
    pass


@when("we move white pawn to f3")
def move_white_pawn_f3(context) -> None:
    """Move white pawn to f3 (1. pf3).

    Args:
        context: The given context of the step.
    """
    chess_engine: ChessEngine = context.chess_engine
    chess_engine.move(FOOLS_MATE_MOVES[0][0], FOOLS_MATE_MOVES[0][1])


@when("we move black pawn to e5")
def move_black_pawn_e5(context) -> None:
    """Move black pawn to e5 (1. pf3 pe5).

    Args:
        context: The given context of the step.
    """
    chess_engine: ChessEngine = context.chess_engine
    for i in range(len(FOOLS_MATE_MOVES) - 2):
        src, dest = FOOLS_MATE_MOVES[i]
        chess_engine.move(src, dest)


@when("we move white pawn to g4")
def move_white_pawn_g4(context) -> None:
    """Move white pawn to g4 (1. pf3 pe5 2. pg4).

    Args:
        context: The given context of the step.
    """
    chess_engine: ChessEngine = context.chess_engine
    for i in range(len(FOOLS_MATE_MOVES) - 1):
        src, dest = FOOLS_MATE_MOVES[i]
        chess_engine.move(src, dest)


@when("we move black queen to h4")
def move_black_queen_h4(context) -> None:
    """Move black queen to h4 (1. pf3 pe5 2. pg4 qh4).

    Args:
        context: The given context of the step.
    """
    chess_engine: ChessEngine = context.chess_engine
    for i in range(len(FOOLS_MATE_MOVES)):
        src, dest = FOOLS_MATE_MOVES[i]
        chess_engine.move(src, dest)


@then("team moves are valid for starting chess position")
def validate_standard_start_move_vectors(context) -> None:
    """Validate black/white move vectors for standard starting position.

    Args:
        context: The given context of the step.
    """
    white: White = context.white
    black: Black = context.black

    WHITE_MOVES = {
        ((6, 0), (5, 0)),
        ((6, 0), (4, 0)),
        ((6, 1), (5, 1)),
        ((6, 1), (4, 1)),
        ((6, 2), (5, 2)),
        ((6, 2), (4, 2)),
        ((6, 3), (5, 3)),
        ((6, 3), (4, 3)),
        ((6, 4), (5, 4)),
        ((6, 4), (4, 4)),
        ((6, 5), (5, 5)),
        ((6, 5), (4, 5)),
        ((6, 6), (5, 6)),
        ((6, 6), (4, 6)),
        ((6, 7), (5, 7)),
        ((6, 7), (4, 7)),
        ((7, 1), (5, 0)),
        ((7, 1), (5, 2)),
        ((7, 6), (5, 5)),
        ((7, 6), (5, 7)),
    }

    BLACK_MOVES = {
        ((1, 0), (2, 0)),
        ((1, 0), (3, 0)),
        ((1, 1), (2, 1)),
        ((1, 1), (3, 1)),
        ((1, 2), (2, 2)),
        ((1, 2), (3, 2)),
        ((1, 3), (2, 3)),
        ((1, 3), (3, 3)),
        ((1, 4), (2, 4)),
        ((1, 4), (3, 4)),
        ((1, 5), (2, 5)),
        ((1, 5), (3, 5)),
        ((1, 6), (2, 6)),
        ((1, 6), (3, 6)),
        ((1, 7), (2, 7)),
        ((1, 7), (3, 7)),
        ((0, 1), (2, 0)),
        ((0, 1), (2, 2)),
        ((0, 6), (2, 5)),
        ((0, 6), (2, 7)),
    }

    assert white.get_moves() == WHITE_MOVES
    assert black.get_moves() == BLACK_MOVES


@then("the team moves are valid for 1. pf3")
def validate_team_moves_1pf3(context) -> None:
    """Validate team moves at game position (1. pf3).

    Args:
        context: The context of the given step.
    """
    white: White = context.white
    black: Black = context.black

    WHITE_MOVES = {
        ((6, 0), (5, 0)),
        ((6, 0), (4, 0)),
        ((6, 1), (5, 1)),
        ((6, 1), (4, 1)),
        ((6, 2), (5, 2)),
        ((6, 2), (4, 2)),
        ((6, 3), (5, 3)),
        ((6, 3), (4, 3)),
        ((6, 4), (5, 4)),
        ((6, 4), (4, 4)),
        ((5, 5), (4, 5)),
        ((6, 6), (5, 6)),
        ((6, 6), (4, 6)),
        ((6, 7), (5, 7)),
        ((6, 7), (4, 7)),
        ((7, 1), (5, 0)),
        ((7, 1), (5, 2)),
        ((7, 6), (5, 7)),
        ((7, 4), (6, 5)),
    }

    BLACK_MOVES = {
        ((1, 0), (2, 0)),
        ((1, 0), (3, 0)),
        ((1, 1), (2, 1)),
        ((1, 1), (3, 1)),
        ((1, 2), (2, 2)),
        ((1, 2), (3, 2)),
        ((1, 3), (2, 3)),
        ((1, 3), (3, 3)),
        ((1, 4), (2, 4)),
        ((1, 4), (3, 4)),
        ((1, 5), (2, 5)),
        ((1, 5), (3, 5)),
        ((1, 6), (2, 6)),
        ((1, 6), (3, 6)),
        ((1, 7), (2, 7)),
        ((1, 7), (3, 7)),
        ((0, 1), (2, 0)),
        ((0, 1), (2, 2)),
        ((0, 6), (2, 5)),
        ((0, 6), (2, 7)),
    }

    assert white.get_moves() == WHITE_MOVES
    assert black.get_moves() == BLACK_MOVES


@then("the team moves are valid for 1. pf3 pe5")
def validate_team_moves_1pf3pe5(context) -> None:
    """Validate team moves at game position 1. pf3 pe5.

    Args:
        context: The context of the given step.
    """
    white: White = context.white
    black: Black = context.black

    WHITE_MOVES = {
        ((6, 0), (5, 0)),
        ((6, 0), (4, 0)),
        ((6, 1), (5, 1)),
        ((6, 1), (4, 1)),
        ((6, 2), (5, 2)),
        ((6, 2), (4, 2)),
        ((6, 3), (5, 3)),
        ((6, 3), (4, 3)),
        ((6, 4), (5, 4)),
        ((6, 4), (4, 4)),
        ((5, 5), (4, 5)),
        ((6, 6), (5, 6)),
        ((6, 6), (4, 6)),
        ((6, 7), (5, 7)),
        ((6, 7), (4, 7)),
        ((7, 1), (5, 0)),
        ((7, 1), (5, 2)),
        ((7, 6), (5, 7)),
        ((7, 4), (6, 5)),
    }

    BLACK_MOVES = {
        ((0, 6), (1, 4)),
        ((0, 4), (1, 4)),
        ((0, 3), (1, 4)),
        ((0, 3), (2, 5)),
        ((0, 3), (3, 6)),
        ((0, 3), (4, 7)),
        ((0, 5), (1, 4)),
        ((0, 5), (2, 3)),
        ((0, 5), (3, 2)),
        ((0, 5), (4, 1)),
        ((0, 5), (5, 0)),
        ((1, 0), (2, 0)),
        ((1, 0), (3, 0)),
        ((1, 1), (2, 1)),
        ((1, 1), (3, 1)),
        ((1, 2), (2, 2)),
        ((1, 2), (3, 2)),
        ((1, 3), (2, 3)),
        ((1, 3), (3, 3)),
        ((3, 4), (4, 4)),
        ((1, 5), (2, 5)),
        ((1, 5), (3, 5)),
        ((1, 6), (2, 6)),
        ((1, 6), (3, 6)),
        ((1, 7), (2, 7)),
        ((1, 7), (3, 7)),
        ((0, 1), (2, 0)),
        ((0, 1), (2, 2)),
        ((0, 6), (2, 5)),
        ((0, 6), (2, 7)),
    }

    assert white.get_moves() == WHITE_MOVES
    assert black.get_moves() == BLACK_MOVES


@then("the team moves are valid for 1. pf3 pe5 2. pg4")
def validate_team_moves_1pf3pe5_2pg4(context) -> None:
    """Validatae team moves for chess position 1. pf3 pe5 2. pg4.

    Args:
        context: The context of the given step.
    """
    white: White = context.white
    black: Black = context.black
    board: Board = context.board
    chess_engine: ChessEngine = context.chess_engine

    WHITE_MOVES = {
        ((6, 0), (5, 0)),
        ((6, 0), (4, 0)),
        ((6, 1), (5, 1)),
        ((6, 1), (4, 1)),
        ((6, 2), (5, 2)),
        ((6, 2), (4, 2)),
        ((6, 3), (5, 3)),
        ((6, 3), (4, 3)),
        ((6, 4), (5, 4)),
        ((6, 4), (4, 4)),
        ((5, 5), (4, 5)),
        ((4, 6), (3, 6)),
        ((6, 7), (5, 7)),
        ((6, 7), (4, 7)),
        ((7, 1), (5, 2)),
        ((7, 1), (5, 0)),
        ((7, 4), (6, 5)),
        ((7, 6), (5, 7)),
        ((7, 5), (5, 7)),
        ((7, 5), (6, 6)),
    }

    BLACK_MOVES = {
        ((0, 6), (1, 4)),
        ((0, 4), (1, 4)),
        ((0, 3), (1, 4)),
        ((0, 3), (2, 5)),
        ((0, 3), (3, 6)),
        ((0, 3), (4, 7)),
        ((0, 5), (1, 4)),
        ((0, 5), (2, 3)),
        ((0, 5), (3, 2)),
        ((0, 5), (4, 1)),
        ((0, 5), (5, 0)),
        ((1, 0), (2, 0)),
        ((1, 0), (3, 0)),
        ((1, 1), (2, 1)),
        ((1, 1), (3, 1)),
        ((1, 2), (2, 2)),
        ((1, 2), (3, 2)),
        ((1, 3), (2, 3)),
        ((1, 3), (3, 3)),
        ((3, 4), (4, 4)),
        ((1, 5), (2, 5)),
        ((1, 5), (3, 5)),
        ((1, 6), (2, 6)),
        ((1, 6), (3, 6)),
        ((1, 7), (2, 7)),
        ((1, 7), (3, 7)),
        ((0, 1), (2, 0)),
        ((0, 1), (2, 2)),
        ((0, 6), (2, 5)),
        ((0, 6), (2, 7)),
    }

    assert white.get_moves() == WHITE_MOVES
    assert black.get_moves() == BLACK_MOVES


@then("the team moves are valid for 1. pf3 pe5 2. pg4 qh4")
def validate_team_moves_1pf3pe5_2pg4(context) -> None:
    """Validatae team moves for chess position 1. pf3 pe5 2. pg4 qh4.

    Args:
        context: The context of the given step.
    """
    white: White = context.white
    black: Black = context.black
    board: Board = context.board
    chess_engine: ChessEngine = context.chess_engine

    BLACK_MOVES = {
        ((0, 6), (1, 4)),
        ((0, 4), (1, 4)),
        ((0, 5), (1, 4)),
        ((0, 5), (2, 3)),
        ((0, 5), (3, 2)),
        ((0, 5), (4, 1)),
        ((0, 5), (5, 0)),
        ((1, 0), (2, 0)),
        ((1, 0), (3, 0)),
        ((1, 1), (2, 1)),
        ((1, 1), (3, 1)),
        ((1, 2), (2, 2)),
        ((1, 2), (3, 2)),
        ((1, 3), (2, 3)),
        ((1, 3), (3, 3)),
        ((3, 4), (4, 4)),
        ((1, 5), (2, 5)),
        ((1, 5), (3, 5)),
        ((1, 6), (2, 6)),
        ((1, 6), (3, 6)),
        ((1, 7), (2, 7)),
        ((1, 7), (3, 7)),
        ((0, 1), (2, 0)),
        ((0, 1), (2, 2)),
        ((0, 6), (2, 5)),
        ((0, 6), (2, 7)),
        ((4, 7), (2, 7)),
        ((4, 7), (3, 7)),
        ((4, 7), (5, 7)),
        ((4, 7), (6, 7)),
        ((4, 7), (5, 6)),
        ((4, 7), (6, 5)),
        ((4, 7), (7, 4)),
        ((4, 7), (4, 6)),
        ((4, 7), (3, 6)),
        ((4, 7), (2, 5)),
        ((4, 7), (1, 4)),
        ((4, 7), (0, 3)),
        ((0, 4), (0, 3)),
    }

    assert black.get_moves() == BLACK_MOVES


@then("white is in a checkmate position")
def white_is_in_checkmate(context) -> None:
    """Determine if white is in a checkmate position.

    Args:
        context: The context of the given step
    """
    white: White = context.white
    black: Black = context.black
    chess_engine: ChessEngine = context.chess_engine

    assert chess_engine.is_check(white, black) is True
    assert chess_engine.is_checkmate(white) is True
