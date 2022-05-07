from src.utils.chess_board_reader import ChessBoardReader

CHESS_BOARDS_DIR = "./tests/test_pawn/chessboards/"


def test_pawn_double_move(chess_board_reader: ChessBoardReader) -> None:
    board = chess_board_reader.read_chess_board(
        file_path=f"{CHESS_BOARDS_DIR}pawn-double-move.txt"
    )
    black_pawn_moves = board._get_piece((1, 0)).get_moves()
    white_pawn_moves = board._get_piece((6, 0)).get_moves()
    assert black_pawn_moves == {(2, 0), (3, 0)}
    assert white_pawn_moves == {(5, 0), (4, 0)}


def test_pawn_capture(chess_board_reader: ChessBoardReader) -> None:
    board = chess_board_reader.read_chess_board(
        file_path=f"{CHESS_BOARDS_DIR}pawn-capture.txt"
    )
    black_pawn_moves = board._get_piece((3, 1)).get_moves()
    white_pawn_moves = board._get_piece((4, 0)).get_moves()
    assert (4, 0) in black_pawn_moves
    assert (3, 1) in white_pawn_moves
