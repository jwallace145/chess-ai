from unittest.mock import NonCallableMagicMock
from art import text2art
from dataclasses import dataclass
from src.board import Board
from typing import List, Tuple
from src.constants import NUM_OF_ROWS
from src.constants import Color

COL_TO_INT = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}


@dataclass
class TerminalEngine:
    def __post_init__(self) -> None:
        self.board = Board()
        self.turn = Color.WHITE

    def _find_piece(self, piece: str, coordinates: Tuple[int, int]) -> Tuple[int, int]:
        pass

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

    def run(self) -> None:
        print(text2art("Chess!"))

        while True:
            print(f"{self.turn.name}'s turn")
            self.board.print_board()
            piece, dest_coordinates = self._get_move_from_user()
            src_coordintates = self.board.find_piece_coordinates(
                piece, dest_coordinates
            )
            print(src_coordintates)
            self.board.move_piece(src_coordintates, dest_coordinates)
            self.turn = Color.BLACK if self.turn == Color.WHITE else Color.WHITE
