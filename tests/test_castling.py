from tests.utils.chess_board_reader import ChessBoardReader
from src.constants import Color


class TestCastling:
    def test_white_kingside_castle(self, chess_board_reader: ChessBoardReader) -> None:
        board = chess_board_reader.read_chess_board(
            "./tests/chessboards/white-kingside-castle.txt"
        )
        possible_castles = board.get_valid_castles()
        # assert len(possible_castles) == 1
        # assert possible_castles[0].color == Color.WHITE
        # assert possible_castles[0].coordinates == (7, 7)
