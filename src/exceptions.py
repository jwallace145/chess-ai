from typing import Tuple


class InvalidCoordinates(Exception):
    def __init__(self, row: int, col: int) -> None:
        super().__init__(f"Coordinates ({row}, {col}) are invalid!")


class InvalidMove(Exception):
    def __init__(self, coordinates: Tuple[int, int]) -> None:
        row, col = coordinates
        super().__init__(f"({row}, {col}) is an invalid move!")


class InvalidColumnUserInput(Exception):
    def __init__(self, col: int) -> None:
        super().__init__(
            f"Column {col} is not a valid column input. Please use a column A - H (not case sensitive)."
        )


class InvalidRowUserInput(Exception):
    def __init__(self, row: int) -> None:
        super().__init__(
            f"Row {row} is not a valid row input. Please use a row between 1 and 8 (inclusive)."
        )


class InvalidPieceUserInput(Exception):
    def __init__(self, piece_enum: str) -> None:
        super().__init__(
            f"Piece {piece_enum} is not a valid piece input. Please use piece input P, R, K, B, Q, K (not case sensitive)."
        )


class InvalidUserInput(Exception):
    def __init__(self, move: list) -> None:
        super().__init__(f"Move {move} is an invalid user input.")


class InvalidCoordinatesUserInput(Exception):
    def __init__(self, coordinates: str) -> None:
        super().__init__(f"Coordinates {coordinates} is an invalid user input.")
