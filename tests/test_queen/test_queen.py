from src.utils.chess_board_reader import ChessBoardReader

CHESS_BOARDS_DIR = "./tests/test_queen/chessboards/"


def test_queen_move(chess_board_reader: ChessBoardReader) -> None:
    board = chess_board_reader.read_chess_board(
        file_path=f"{CHESS_BOARDS_DIR}queen-move.txt"
    )
    black_queen_moves = board._get_piece((1, 2)).get_moves()
    white_queen_moves = board._get_piece((5, 3)).get_moves()
    assert black_queen_moves == {
        (0, 2),
        (2, 2),
        (3, 2),
        (4, 2),
        (5, 2),
        (6, 2),
        (7, 2),
        (1, 0),
        (1, 1),
        (1, 3),
        (1, 4),
        (1, 5),
        (1, 6),
        (1, 7),
        (0, 1),
        (2, 3),
        (3, 4),
        (4, 5),
        (5, 6),
        (6, 7),
        (0, 3),
        (2, 1),
        (3, 0),
    }
    assert white_queen_moves == {
        (5, 0),
        (5, 1),
        (5, 2),
        (5, 4),
        (5, 5),
        (5, 6),
        (5, 7),
        (0, 3),
        (1, 3),
        (2, 3),
        (3, 3),
        (4, 3),
        (6, 3),
        (7, 3),
        (7, 1),
        (6, 2),
        (4, 4),
        (3, 5),
        (2, 6),
        (1, 7),
        (7, 5),
        (6, 4),
        (4, 2),
        (3, 1),
        (2, 0),
    }


def test_queen_capture(chess_board_reader: ChessBoardReader) -> None:
    board = chess_board_reader.read_chess_board(
        file_path=f"{CHESS_BOARDS_DIR}queen-capture.txt"
    )
    black_queen_moves = board._get_piece((0, 3)).get_moves()
    white_queen_moves = board._get_piece((7, 3)).get_moves()
    assert black_queen_moves == {(0, 1), (0, 2), (1, 3), (2, 3), (1, 2)}
    assert white_queen_moves == {(7, 0), (7, 1), (7, 2), (6, 3), (5, 3)}
