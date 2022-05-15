from src.utils.chess_board_reader import ChessBoardReader

CHESS_BOARDS_DIR = "./tests/test_rook/chessboards/"


def test_rook_move(chess_board_reader: ChessBoardReader) -> None:
    chess_engine = chess_board_reader.read_chess_board(
        file_path=f"{CHESS_BOARDS_DIR}rook-move.txt"
    )
    black_rook_moves = chess_engine.get_piece((0, 7)).get_moves()
    white_rook_moves = chess_engine.get_piece((7, 0)).get_moves()
    assert black_rook_moves == {
        (0, 6),
        (0, 5),
        (1, 7),
        (2, 7),
        (3, 7),
        (4, 7),
        (5, 7),
        (6, 7),
        (7, 7),
    }
    assert white_rook_moves == {
        (7, 1),
        (7, 2),
        (7, 3),
        (6, 0),
        (5, 0),
        (4, 0),
        (3, 0),
        (2, 0),
        (1, 0),
        (0, 0),
    }


def test_rook_capture(chess_board_reader: ChessBoardReader) -> None:
    chess_engine = chess_board_reader.read_chess_board(
        file_path=f"{CHESS_BOARDS_DIR}rook-capture.txt"
    )
    black_rook_moves = chess_engine.get_piece((1, 6)).get_moves()
    white_rook_moves = chess_engine.get_piece((6, 1)).get_moves()
    assert black_rook_moves == {(1, 5), (1, 4), (1, 7), (0, 6), (2, 6), (3, 6)}
    assert white_rook_moves == {
        (5, 1),
        (4, 1),
        (3, 1),
        (6, 2),
        (6, 3),
        (6, 4),
        (7, 1),
        (6, 0),
    }


def test_cannot_move_rook_into_check(chess_board_reader: ChessBoardReader) -> None:
    chess_engine = chess_board_reader.read_chess_board(
        file_path=f"{CHESS_BOARDS_DIR}cannot-move-rook-into-check.txt"
    )
    white_rook_moves = chess_engine.get_piece((7, 3)).get_moves()
    assert white_rook_moves == {(7, 0), (7, 1), (7, 2)}
