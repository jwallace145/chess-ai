from tests.utils.chess_board_reader import ChessBoardReader
import pytest
from src.exceptions import InvalidMove


class TestPawnMoves:
    def test_pawn_double_move(self, chess_board_reader: ChessBoardReader) -> None:
        board = chess_board_reader.read_chess_board(
            "./tests/chessboards/start-position.txt"
        )
        board.move_piece((6, 0), (4, 0))
        board.move_piece((1, 1), (3, 1))
        with pytest.raises(InvalidMove):
            board.move_piece((4, 0), (2, 0))
