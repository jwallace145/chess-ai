from tests.utils.chess_board_reader import ChessBoardReader
import pytest
from src.exceptions import InvalidMove


class TestKingMoves:
    def test_cannot_move_into_check(self, chess_board_reader: ChessBoardReader) -> None:
        board = chess_board_reader.read_chess_board(
            "./tests/chessboards/move-into-check.txt"
        )
        moves = board.get_moves((7, 4))
        assert len(moves) == 1
        assert (6, 4) in moves
