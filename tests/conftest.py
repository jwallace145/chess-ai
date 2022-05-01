import pytest

from tests.utils.chess_board_reader import ChessBoardReader


@pytest.fixture
def chess_board_reader() -> ChessBoardReader:
    return ChessBoardReader()
