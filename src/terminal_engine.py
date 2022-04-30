import os
from dataclasses import dataclass
from time import sleep
from typing import List, Tuple

from art import text2art

from src.board import Board
from src.constants import NUM_OF_ROWS, Color, PieceEnum
from src.exceptions import (
    InvalidColumnUserInput,
    InvalidCoordinatesUserInput,
    InvalidMove,
    InvalidPieceUserInput,
    InvalidRowUserInput,
    InvalidUserInput,
)

COL_TO_INT = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
STR_TO_PIECEENUM = {
    "p": PieceEnum.PAWN,
    "r": PieceEnum.ROOK,
    "b": PieceEnum.BISHOP,
    "n": PieceEnum.KNIGHT,
    "q": PieceEnum.QUEEN,
    "k": PieceEnum.KING,
}


@dataclass
class TerminalEngine:
    def __post_init__(self) -> None:
        self.board = Board()

    def _convert_coordinates(self, coordinates: str) -> Tuple[int, int]:
        if len(coordinates) != 2:
            raise InvalidCoordinatesUserInput(coordinates)
        col, row = coordinates

        if col.lower() not in COL_TO_INT:
            raise InvalidColumnUserInput(col)

        if int(row) < 1 or int(row) > NUM_OF_ROWS:
            raise InvalidRowUserInput(row)

        col = COL_TO_INT[col.lower()]
        row = -1 * int(row) + NUM_OF_ROWS

        return (row, col)

    def _get_move_from_user(self) -> Tuple[PieceEnum, Tuple[int, int]]:
        move = input("\n\nMOVE: ").strip().split(" ")

        # remove spaces
        spaces = move.count("")
        for _ in range(spaces):
            move.remove("")

        if len(move) != 2:
            raise InvalidUserInput(move)

        piece, coordinates = move

        if piece.lower() not in STR_TO_PIECEENUM:
            raise InvalidPieceUserInput(piece)

        coordinates = self._convert_coordinates(coordinates)

        return (STR_TO_PIECEENUM[piece.lower()], coordinates)

    def _move_piece(
        self, piece_enum: PieceEnum, dest_coordinates: Tuple[int, int]
    ) -> None:
        try:
            piece = self.board.find_piece(piece_enum, dest_coordinates)
            self.board.move_piece(piece.coordinates, dest_coordinates)
            if self.board.is_check():
                print("CHECK!")
                sleep(3)
                if self.board.is_checkmate():
                    print("CHECKMATE")
                    sleep(3)
        except InvalidMove as e:
            print(e)
            sleep(5)

    def run(self) -> None:
        while True:
            os.system("cls||clear")
            print(text2art("Chess!"))
            self.board.print_board()
            while True:
                try:
                    piece, dest_coordinates = self._get_move_from_user()
                    break
                except InvalidUserInput as e:
                    print(e)
                except InvalidPieceUserInput as e:
                    print(e)
                except InvalidColumnUserInput as e:
                    print(e)
                except InvalidRowUserInput as e:
                    print(e)
                except InvalidCoordinatesUserInput as e:
                    print(e)
            self._move_piece(piece, dest_coordinates)
