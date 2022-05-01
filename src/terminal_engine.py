import os
from dataclasses import dataclass
from typing import Tuple
from src.utils import print_board

from art import text2art

from src.board import Board
from src.constants import COLUMNS, NUM_OF_COLS, NUM_OF_ROWS, PIECES, Color
from src.exceptions import (
    InvalidColumnUserInput,
    InvalidCoordinatesUserInput,
    InvalidMove,
    InvalidPieceUserInput,
    InvalidRowUserInput,
    InvalidUserInput,
)
from src.pieces.piece import Piece


@dataclass
class TerminalEngine:
    """Terminal Chess Engine"""

    def __post_init__(self) -> None:
        self.board = Board()
        self.board.initialize()

    def _convert_coordinates(self, coordinates: str) -> Tuple[int, int]:
        """Convert coordinates of syntax e.g. e4 to row, col coordinates e.g. (4, 4).

        Args:
            coordinates (str): The coordinates in string format.

        Raises:
            InvalidCoordinatesUserInput: Raises InvalidCoordinatesUserInput if more than row, col is provided as coordinates.
            InvalidColumnUserInput: Raises InvalidColumnUserInput if given column in string format is not within range a - g.
            InvalidRowUserInput: Raises InvalidRowUserInput if given row isnt within range [1, 8].

        Returns:
            Tuple[int, int]: The coordinates in row, col format.
        """
        if len(coordinates) != 2:
            raise InvalidCoordinatesUserInput(coordinates)

        col, row = coordinates

        if col.lower() not in COLUMNS:
            raise InvalidColumnUserInput(col)

        if int(row) < 1 or int(row) > NUM_OF_ROWS:
            raise InvalidRowUserInput(row)

        col = COLUMNS[col.lower()]
        row = -1 * int(row) + NUM_OF_ROWS

        return (row, col)

    def _get_move_from_user(self) -> Tuple[Piece, Tuple[int, int]]:
        """Get move from user input.

        Raises:
            InvalidUserInput: Raises InvalidUserInput if more than desired piece and destination
                              coordinates are given
            InvalidPieceUserInput: Raises InvalidPieceUserInput if piece outside the set of pieces
                                   is given.

        Returns:
            Tuple[Piece, Tuple[int, int]]: The chess piece to move and the destination coordinates.
        """
        # delimit by spaces and remove empty "" elements from list
        move = [i for i in input("\n\nMOVE: ").strip().split(" ") if i != ""]

        # ensure length of list is 2 e.g. piece and dest coordinates
        if len(move) != 2:
            raise InvalidUserInput(move)

        piece, coordinates = move

        # ensure lowercase piece is a valid piece
        if piece.lower() not in PIECES:
            raise InvalidPieceUserInput(piece)

        # covert coordinates from e4 to (4, 4) for example
        coordinates = self._convert_coordinates(coordinates)

        # get chess piece
        piece = self.board.find_piece(PIECES[piece.lower()], coordinates)

        return piece, coordinates

    def _move_piece(self, piece: Piece, dest_coordinates: Tuple[int, int]) -> None:
        """Move chess piece to destination.

        Args:
            piece (Piece): The given chess piece
            dest_coordinates (Tuple[int, int]): The desired destination of the chess piece.
        """
        try:
            self.board.move_piece(piece.coordinates, dest_coordinates)
        except InvalidMove as e:
            print(e)

    def _endgame(self) -> bool:
        """Determines whether the given game is in an end state or not.

        Returns:
            bool: True if the game is in an end state. Otherwise, False.
        """
        return self.board.is_check() and self.board.is_checkmate()

    def run(self) -> None:
        """Run the chess engine.

        Play a PvP game of chess until a checkmate.
        """
        while not self._endgame():
            os.system("cls||clear")
            print(text2art("Chess!"))

            print_board(self.board)

            # get user input until valid move is given
            while True:
                try:
                    piece, dest_coordinates = self._get_move_from_user()
                    break
                except Exception as e:
                    print(e)

            # move piece
            self._move_piece(piece, dest_coordinates)

        os.system("cls||clear")
        print(text2art("Checkmate!"))

        print_board(self.board)

        winner = Color.BLACK if self.board._turn == Color.WHITE else Color.WHITE

        print(text2art(f"\n\n{winner.name} wins"))
