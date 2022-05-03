from dataclasses import dataclass

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
    def read_chess_board(
        self, file_path: str, current_team: Color = Color.WHITE
    ) -> Board:
        self._board = Board()
        self._black = Black()
        self._white = White()
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
                            PIECES[piece.lower()],
                            PIECE_CONSTRUCTORS[piece.lower()](Color.BLACK, (row, col)),
                        )
                    elif team == Color.WHITE.value:
                        self._white.add_piece(
                            PIECES[piece.lower()],
                            PIECE_CONSTRUCTORS[piece.lower()](Color.WHITE, (row, col)),
                        )

        current = self._white if current_team == Color.WHITE else self._black
        opposing = self._black if current_team == Color.WHITE else self._white
        self._board.initialize(self._black, self._white, current, opposing)

        return self._board
