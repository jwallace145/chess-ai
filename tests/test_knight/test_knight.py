from src.utils.chess_board_reader import ChessBoardReader

CHESS_BOARDS_DIR = "./tests/test_knight/chessboards/"


def test_knight_move(chess_board_reader: ChessBoardReader) -> None:
    board = chess_board_reader.read_chess_board(
        file_path=f"{CHESS_BOARDS_DIR}knight-move.txt"
    )
    black_knight_moves = board._get_piece((2, 2)).get_moves()
    white_knight_moves = board._get_piece((5, 2)).get_moves()
    assert black_knight_moves == {
        (4, 3),
        (4, 1),
        (0, 3),
        (0, 1),
        (1, 4),
        (3, 4),
        (1, 0),
        (3, 0),
    }
    assert white_knight_moves == {
        (3, 3),
        (3, 1),
        (7, 1),
        (7, 3),
        (4, 4),
        (6, 4),
        (4, 0),
        (6, 0),
    }


def test_knight_capture(chess_board_reader: ChessBoardReader) -> None:
    board = chess_board_reader.read_chess_board(
        file_path=f"{CHESS_BOARDS_DIR}knight-capture.txt"
    )
    black_knight_moves = board._get_piece((2, 2)).get_moves()
    white_knight_moves = board._get_piece((5, 2)).get_moves()
    assert black_knight_moves == {
        (4, 3),
        (4, 1),
        (0, 3),
        (0, 1),
        (1, 4),
        (3, 4),
        (3, 0),
    }
    assert white_knight_moves == {
        (3, 3),
        (3, 1),
        (7, 1),
        (7, 3),
        (4, 4),
        (6, 4),
        (4, 0),
    }
