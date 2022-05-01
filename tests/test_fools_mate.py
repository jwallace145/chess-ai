from tests.utils.chess_board_reader import ChessBoardReader


class TestFoolsMate:
    def test_fools_mate(self, chess_board_reader: ChessBoardReader) -> None:
        """Test the quickest checkmate possible: The Fool's Mate."""
        board = chess_board_reader.read_chess_board(
            "./tests/chessboards/fools-mate.txt"
        )
        assert board.is_check() is True
        assert board.is_checkmate() is True
