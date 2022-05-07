import os
from dataclasses import dataclass
from typing import Tuple

from art import text2art
from simple_term_menu import TerminalMenu

from src.board import Board
from src.constants import PIECES, MenuOption
from src.exceptions import InvalidMove, InvalidPieceUserInput, InvalidUserInput
from src.pieces.piece import Piece
from src.utils.utils import convert_coordinates


@dataclass
class TerminalEngine:
    """Terminal Chess Engine"""

    def __post_init__(self) -> None:
        self.board = Board()

        # initialize board with standard configs
        self.board.initialize()

    def _options_menu(self) -> str:
        print("\n\n")
        options = [MenuOption.MOVE_A_PIECE.value, MenuOption.GET_VALID_MOVES.value]
        options_menu = TerminalMenu(options)
        menu_entry_index = options_menu.show()
        return options[menu_entry_index]

    def _get_valid_moves(self) -> None:
        # get user input until valid move is given
        while True:
            try:
                # delimit by spaces and remove empty "" elements from list
                piece = [i for i in input("\n\nPIECE: ").strip().split(" ") if i != ""]

                # ensure length of list is 2 e.g. piece and dest coordinates
                if len(piece) != 2:
                    raise InvalidUserInput(piece)

                piece, coordinates = piece

                # ensure lowercase piece is a valid piece
                if piece.lower() not in PIECES:
                    raise InvalidPieceUserInput(piece)

                # covert coordinates from e4 to (4, 4) for example
                coordinates = convert_coordinates(coordinates)

                piece = self.board._get_piece(coordinates)

                print(f"\nVALID MOVES: {piece.get_valid_moves()}")

                input("press enter to continue...")
                break
            except Exception as e:
                print(e)

    def _move_a_piece(self) -> None:
        # get user input until valid move is given
        while True:
            try:
                piece, dest_coordinates = self._get_move_from_user()
                break
            except Exception as e:
                print(e)

        # move piece
        self._move_piece(piece, dest_coordinates)

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

            self.board.print_board()

            option = self._options_menu()

            if option is MenuOption.MOVE_A_PIECE.value:
                self._move_a_piece()
            elif option is MenuOption.GET_VALID_MOVES.value:
                self._get_valid_moves()

        os.system("cls||clear")
        print(text2art("Checkmate!"))

        self.board.print_board()

        print(text2art(f"\n\n{self.board._opposing_team.color.name} wins :)"))
