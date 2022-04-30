import os
from time import sleep
from art import text2art
from dataclasses import dataclass
from src.board import Board
from typing import List, Tuple
from src.constants import NUM_OF_ROWS
from src.constants import Color
from src.exceptions import InvalidMove

COL_TO_INT = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}


@dataclass
class TerminalEngine:
    def __post_init__(self) -> None:
        self.board = Board()
        self.turn = Color.WHITE

    def _convert_coordinates(self, coordinates: str) -> Tuple[int, int]:
        col, row = coordinates

        col = COL_TO_INT[col.lower()]
        row = -1 * int(row) + NUM_OF_ROWS

        return (row, col)

    def _get_move_from_user(self) -> Tuple[str, Tuple[int, int]]:
        move = input("\nMOVE: ").strip().split(" ")

        # remove spaces
        spaces = move.count("")
        for s in range(spaces):
            move.remove("")

        piece, coordinates = move
        coordinates = self._convert_coordinates(coordinates)

        return (piece, coordinates)

    def _move_piece(self, piece: str, dest_coordinates: Tuple[int, int]) -> None:
        try:
            src_coordinates = self.board.find_piece_coordinates(piece, dest_coordinates)
            self.board.move_piece(src_coordinates, dest_coordinates)
            if self.board.is_check():
                self.board.is_checkmate()
            sleep(2)
        except InvalidMove as e:
            print(e)
            sleep(5)

    def run(self) -> None:
        while True:
            os.system("cls||clear")
            print(text2art("Chess!"))
            self.board.print_board()
            piece, dest_coordinates = self._get_move_from_user()
            self._move_piece(piece, dest_coordinates)
