import pytest
from src.board import Board
from src.exceptions import InvalidMove


class TestPawnMoves:
    @pytest.fixture(autouse=True)
    def init_test_pawn_moves(self) -> None:
        self.board = Board()

    def test_pawn_double_move(self) -> None:
        for src, dest in [((6, 0), (4, 0)), ((1, 0), (3, 0))]:
            self.board.move_piece(src, dest)

    def test_pawn_double_move_after_move(self) -> None:
        with pytest.raises(InvalidMove):
            for src, dest in [((6, 7), (5, 7)), ((1, 7), (2, 7)), ((5, 7), (3, 7))]:
                self.board.move_piece(src, dest)
