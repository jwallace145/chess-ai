from src.utils.chess_board_reader import ChessBoardReader

CHESS_BOARDS_DIR = "./tests/test_king/chessboards/"


def test_king_move(chess_board_reader: ChessBoardReader) -> None:
    board = chess_board_reader.read_chess_board(
        file_path=f"{CHESS_BOARDS_DIR}king-move.txt"
    )
    black_king_moves = board._get_piece((1, 4)).get_moves()
    white_king_moves = board._get_piece((6, 4)).get_moves()
    assert black_king_moves == {
        (1, 3),
        (1, 5),
        (0, 4),
        (2, 4),
        (0, 5),
        (0, 3),
        (2, 3),
        (2, 5),
    }
    assert white_king_moves == {
        (6, 5),
        (6, 3),
        (5, 4),
        (7, 4),
        (7, 5),
        (7, 3),
        (5, 5),
        (5, 3),
    }


def test_king_capture(chess_board_reader: ChessBoardReader) -> None:
    board = chess_board_reader.read_chess_board(
        file_path=f"{CHESS_BOARDS_DIR}king-capture.txt"
    )
    black_king_moves = board._get_piece((0, 4)).get_moves()
    white_king_moves = board._get_piece((7, 4)).get_moves()
    assert black_king_moves == {(1, 4), (0, 3), (0, 5), (1, 3), (1, 5)}
    assert white_king_moves == {(6, 4), (7, 3), (7, 5), (6, 3), (6, 5)}


def test_cannot_move_king_into_check(chess_board_reader: ChessBoardReader) -> None:
    board = chess_board_reader.read_chess_board(
        file_path=f"{CHESS_BOARDS_DIR}cannot-move-king-into-check.txt"
    )
    assert False
