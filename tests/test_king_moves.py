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

    def test_no_valid_king_moves_but_can_escape_check(
        self, chess_board_reader: ChessBoardReader
    ) -> None:
        board = chess_board_reader.read_chess_board(
            "./tests/chessboards/escape-check-no-valid-king-moves.txt"
        )
        assert board.is_checkmate() is False
