from typing import Tuple


class TileIsOccupied(Exception):
    def __init__(self, row: int, col: int) -> None:
        super().__init__(f"Tile ({row}, {col}) is currently occupied!")


class InvalidCoordinates(Exception):
    def __init__(self, row: int, col: int) -> None:
        super().__init__(f"Coordinates ({row}, {col}) are invalid!")


class InvalidMove(Exception):
    def __init__(self, coordinates: Tuple[int, int]) -> None:
        row, col = coordinates
        super().__init__(f"({row}, {col}) is an invalid move!")
