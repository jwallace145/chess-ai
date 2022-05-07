from dataclasses import dataclass, field

from src.board import Board
from src.constants import NUM_OF_COLS, NUM_OF_ROWS, PIECES, Color
from src.pieces.bishop import Bishop
from src.pieces.king import King
from src.pieces.knight import Knight
from src.pieces.pawn import Pawn
from src.pieces.queen import Queen
from src.pieces.rook import Rook
from src.teams.black import Black
from src.teams.team import Team
from src.teams.white import White

PIECE_CONSTRUCTORS = {
    "p": Pawn,
    "r": Rook,
    "n": Knight,
    "b": Bishop,
    "q": Queen,
    "k": King,
}


@dataclass
class ChessBoardReader:
    """Chess Board Reader"""

    _board: Board = field(default_factory=lambda: Board())
    _black: Team = field(default_factory=lambda: Black())
    _white: Team = field(default_factory=lambda: White())

    def read_chess_board(
        self, file_path: str, current_team: Color = Color.WHITE
    ) -> Board:
        """Reads text file and returns chess board object with given configurations.

        Args:
            file_path (str): The file path to the text file chess board.
            current_team (Color, optional): The current team of the chess board. Defaults to Color.WHITE.

        Returns:
            Board: The chess board that represents the given configurations.
        """
        # loop over text chess board and create white and black teams
        chessboard = []
        for row in open(file_path, "r").readlines():
            # read squares and remove empty elements and newline characters
            chessboard.append(
                [
                    square.strip()
                    for square in row.split("|")
                    if square != "" and square != "\n"
                ]
            )

        # create black and white teams
        for row in range(NUM_OF_ROWS):
            for col in range(NUM_OF_COLS):
                square = chessboard[row][col]

                if square != "--":
                    team, piece = square
                    if team == Color.BLACK.value:
                        self._black.add_piece(
                            PIECE_CONSTRUCTORS[piece.lower()](Color.BLACK, (row, col)),
                        )
                    elif team == Color.WHITE.value:
                        self._white.add_piece(
                            PIECE_CONSTRUCTORS[piece.lower()](Color.WHITE, (row, col)),
                        )

        current = self._white if current_team == Color.WHITE else self._black
        self._board.initialize(self._black, self._white, current)

        return self._board
