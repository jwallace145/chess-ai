import pytest
from src.board import Board


class TestFoolsMate:
    @pytest.fixture(autouse=True)
    def init_test_fools_mate(self) -> None:
        self.board = Board()

    def test_fools_mate(self) -> None:
        """Test the quickest checkmate possible: The Fool's Mate."""
        assert self.board.is_check() is False
        self.board.move_piece((6, 5), (5, 5))
        self.board.move_piece((1, 4), (3, 4))
        self.board.move_piece((6, 6), (4, 6))
        self.board.move_piece((0, 3), (4, 7))
        assert self.board.is_check() is True
        assert self.board.is_checkmate() is True
