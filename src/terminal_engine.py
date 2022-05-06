import os
from dataclasses import dataclass
from typing import Tuple

from art import text2art

from src.board import Board
from src.constants import PIECES
from src.exceptions import (
    InvalidMove,
    InvalidPieceUserInput,
    InvalidUserInput,
)
from src.pieces.piece import Piece
from src.utils.utils import print_board, convert_coordinates


@dataclass
class TerminalEngine:
    """Terminal Chess Engine"""

    def __post_init__(self) -> None:
        self.board = Board()

        # initialize board with standard configs
        self.board.initialize()

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
        coordinates = convert_coordinates(coordinates)

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
            print(piece)
            self.board.move_piece(piece, dest_coordinates)
        except InvalidMove as error:
            print(error)

    def run(self) -> None:
        """Run the chess engine.

        Play a PvP game of chess until a checkmate.
        """
        while not self.board.is_checkmate():
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

        print(text2art(f"\n\n{self.board._opposing_team.color.name} wins :)"))
