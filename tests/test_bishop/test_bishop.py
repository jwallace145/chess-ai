from src.utils.chess_board_reader import ChessBoardReader

CHESS_BOARDS_DIR = "./tests/test_bishop/chessboards/"


def test_bishop_move(chess_board_reader: ChessBoardReader) -> None:
    board = chess_board_reader.read_chess_board(
        file_path=f"{CHESS_BOARDS_DIR}bishop-move.txt"
    )
    black_bishop_moves = board._get_piece((1, 1)).get_moves()
    white_bishop_moves = board._get_piece((6, 1)).get_moves()
    assert black_bishop_moves == {
        (0, 0),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (2, 0),
        (0, 2),
    }
    assert white_bishop_moves == {
        (7, 0),
        (5, 2),
        (4, 3),
        (3, 4),
        (2, 5),
        (1, 6),
        (0, 7),
        (7, 2),
        (5, 0),
    }


def test_bishop_capture(chess_board_reader: ChessBoardReader) -> None:
    board = chess_board_reader.read_chess_board(
        file_path=f"{CHESS_BOARDS_DIR}bishop-capture.txt"
    )
    black_bishop_moves = board._get_piece((1, 1)).get_moves()
    white_bishop_moves = board._get_piece((6, 1)).get_moves()
    assert black_bishop_moves == {(2, 2), (3, 3), (2, 0), (0, 2)}
    assert white_bishop_moves == {
        (5, 2),
        (4, 3),
        (7, 2),
        (5, 0),
    }
