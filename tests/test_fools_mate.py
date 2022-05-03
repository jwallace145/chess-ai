from tests.utils.chess_board_reader import ChessBoardReader
from src.constants import Color


class TestFoolsMate:
    def test_fools_mate_black(self, chess_board_reader: ChessBoardReader) -> None:
        """Test the quickest black checkmate possible: The Fool's Mate."""
        board = chess_board_reader.read_chess_board(
            "./tests/chessboards/fools-mate-black.txt", Color.WHITE
        )
        assert board.is_checkmate() is True

    def test_fools_mate_white(self, chess_board_reader: ChessBoardReader) -> None:
        """Test the quickest white checkmate possible: The Fool's Mate."""
        board = chess_board_reader.read_chess_board(
            "./tests/chessboards/fools-mate-white.txt", Color.BLACK
        )
        assert board.is_checkmate() is True
