from dataclasses import dataclass, field

from src.board import Board
from src.chess_engine import ChessEngine
from src.constants import NUM_OF_COLS, NUM_OF_ROWS, Color
from src.pieces.bishop import Bishop
from src.pieces.king import King
from src.pieces.knight import Knight
from src.pieces.pawn import Pawn
from src.pieces.queen import Queen
from src.pieces.rook import Rook
from src.teams.black import Black
from src.teams.team import Team
from src.teams.white import White
from collections import defaultdict

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
    _black: Team = field(default_factory=lambda: Black(pieces=defaultdict(set)))
    _white: Team = field(default_factory=lambda: White(pieces=defaultdict(set)))

    def read_chess_board(
        self, file_path: str, current_team: Color = Color.WHITE
    ) -> ChessEngine:
        """Reads text file and returns chess board object with given configurations.

        Args:
            file_path (str): The file path to the text file chess board.
            current_team (Color, optional): The current team of the chess board. Defaults to Color.WHITE.

        Returns:
            ChessEngine: The chess engine with the given teams.
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
                        if team + piece == "BQ":
                            print("black queen")
                        self._black.add_piece(
                            PIECE_CONSTRUCTORS[piece.lower()](Color.BLACK, (row, col)),
                        )
                    elif team == Color.WHITE.value:
                        self._white.add_piece(
                            PIECE_CONSTRUCTORS[piece.lower()](Color.WHITE, (row, col)),
                        )

        chess_engine = ChessEngine(self._black, self._white)

        return chess_engine
