from typing import Tuple

from src.constants import NUM_OF_COLS, NUM_OF_ROWS, PieceEnum
from src.pieces.piece import Piece


class Queen(Piece):
    def __init__(self, color: str, coordinates: Tuple[int, int]) -> None:
        self.moves = []
        self.moves.append([(0, c) for c in range(1, NUM_OF_COLS)])  # move right
        self.moves.append([(0, -c) for c in range(1, NUM_OF_COLS)])  # move left
        self.moves.append([(r, 0) for r in range(1, NUM_OF_ROWS)])  # move down
        self.moves.append([(-r, 0) for r in range(1, NUM_OF_ROWS)])  # move up
        self.moves.append([(i, i) for i in range(1, NUM_OF_ROWS)])  # diagonal up right
        self.moves.append([(i, -i) for i in range(1, NUM_OF_ROWS)])  # diagonal up left
        self.moves.append(
            [(-i, -i) for i in range(1, NUM_OF_ROWS)]
        )  # diagonal down right
        self.moves.append(
            [(-i, i) for i in range(1, NUM_OF_ROWS)]
        )  # diagonal down left
        super().__init__(PieceEnum.QUEEN, color, coordinates, self.moves, self.moves)
