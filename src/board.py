from dataclasses import dataclass, field
from typing import List, Set, Tuple

from src.constants import NUM_OF_COLS, NUM_OF_ROWS, Color, PieceEnum
from src.exceptions import InvalidMove
from src.pieces.piece import Piece
from src.teams.black import Black
from src.teams.team import Team
from src.teams.white import White


@dataclass
class Board:
    """Chess Board Class"""

    _black: Team = Black()
    _white: Team = White()
    _board: List[List[Piece]] = field(
        default_factory=lambda: [
            [None for _ in range(NUM_OF_COLS)] for _ in range(NUM_OF_ROWS)
        ]
    )

    def initialize(
        self, black: Black = None, white: White = None, current_team: Team = None
    ) -> None:
        """Initialize black and white teams and set the board.

        Set the black and white teams as well as the current team. Black and white teams
        can be overridden for a nondefault configuration.

        Args:
            black (Black, optional): The black team. Defaults to None.
            white (White, optional): The white team. Defaults to None.
            current_team (Team, optional): The current team to make a move. Defaults to None.
        """
        # initialize black and white teams, override default if black/white provided
        self._black = black if black else self._black.initialize()
        self._white = white if white else self._white.initialize()
        self._current_team = current_team if current_team else self._white
        self._opposing_team = (
            self._black if self._current_team == self._white else self._white
        )

        # place black and white pieces on board
        pieces = self._black.get_all_pieces().union(self._white.get_all_pieces())
        for piece in pieces:
            self._place_piece(piece, piece.coordinates)

        # calculate valid moves for opposing and current team
        self._calculate_team_moves(self._opposing_team)
        self._calculate_team_moves(self._current_team)

    def _calculate_team_moves(self, team: Team) -> None:
        """Calculate moves for a given team.

        This method calculates all moves for a given team and should be called every
        time the board is updated. Calculating the opposing team's moves first is ideal
        in order to determine check and checkmate positions for current team.

        Args:
            team (Team): The given team. Black or White.
        """
        for piece in team.get_all_pieces():
            moves = self._calculate_piece_moves(piece)
            piece.set_moves(moves)

    def _move_piece(self, piece: Piece, dest: Tuple[int, int]) -> None:
        self._pickup_piece(piece)
        if self._is_vacant(dest):
            self._place_piece(piece, dest)
        elif self._is_capture(piece, dest):
            self._capture_piece(piece, dest)

    def _is_vacant(self, coordinates: Tuple[int, int]) -> bool:
        """Determine if the given cell is vacant or occupied.

        Args:
            coordinates (Tuple[int, int]): The coordinates of the cell.

        Returns:
            bool: True if the cell is currently vacant. Otherwise, False.
        """
        row, col = coordinates
        if self._board[row][col] is None:
            return True
        return False

    def _is_capture(self, piece: Piece, dest: Tuple[int, int]) -> bool:
        """Determine if moving the piece to the given destination cell is an enemy capture.

        Args:
            piece (Piece): The given chess piece.
            dest (Tuple[int, int]): The destination coordinates of possible enemy capture.

        Returns:
            bool: True if moving the given piece to the destination coordinates captures an enemy piece. Otherwise, False.
        """
        enemy = self._get_piece(dest)
        if enemy and enemy.color != piece.color:
            return True
        return False

    def _get_piece(self, coordinates: Tuple[int, int]) -> Piece:
        """Get the chess piece at the given coordinates. Do not remove chess piece.

        Args:
            coordinates (Tuple[int, int]): The coordinates of the chess piece.

        Returns:
            Piece: The chess piece at given coordinates. If no chess piece exists at
                   the given coordinates return None.
        """
        row, col = coordinates
        return self._board[row][col]

    def _pickup_piece(
        self, piece: Piece = None, coordinates: Tuple[int, int] = None
    ) -> Piece:
        """Pick up and remove chess piece from given coordinates and return the chess piece.

        Args:
            coordinates (Tuple[int, int]): The coordinates of the chess piece.

        Returns:
            Piece: The chess piece at the given coordinates.
        """
        if piece:
            row, col = piece.coordinates
            self._board[row][col] = None
            return piece
        elif coordinates:
            row, col = coordinates
            piece = self._board[row][col]
            self._board[row][col] = None
            return piece
        else:
            raise Exception

    def _capture_piece(self, piece: Piece, dest: Tuple[int, int]) -> Piece:
        captured_piece = self._get_piece(dest)
        self._opposing_team.remove_piece(captured_piece)
        self._place_piece(piece, dest)
        return captured_piece

    def _place_piece(self, piece: Piece, dest: Tuple[int, int]) -> None:
        """Place chess piece at the given coordinates.

        This method does not check that the given coordinates are a valid move for the given piece.
        This method updates the piece coordinates and places the piece on the board.

        Args:
            piece (Piece): The chess piece.
            dest (Tuple[int, int]): The desired coordinates.
        """
        piece.coordinates = dest
        row, col = dest
        self._board[row][col] = piece

    def find_piece(self, piece: PieceEnum, dest: Tuple[int, int]) -> Piece:
        """Find chess piece given the type of chess piece and destination coordinates.

        This method is helpful for finding the desired chess piece given a move in the
        syntax "P E4". This means move current team Pawn to square E4 (4,4).

        Args:
            piece (PieceEnum): The type of chess piece
            dest (Tuple[int, int]): The destination coordinates of the given chess piece.

        Raises:
            InvalidMove: Raises an InvalidMove exception if none of the current team pieces can move to the
                         given destination square.

        Returns:
            Piece: The chess piece that can make to the given destination square.
        """
        possible_pieces = []
        for piece in self._current_team.get_pieces(piece):
            if dest in piece.get_moves():
                possible_pieces.append(piece)

        if len(possible_pieces) == 0:
            raise InvalidMove(dest)
        elif len(possible_pieces) == 1:
            return possible_pieces[0]
        else:
            print("MULTIPLE PIECES FOUND NOT GOOD")
            return possible_pieces[0]

    def print_board(self) -> None:
        """Print current chess board to terminal."""
        print(f"Current turn: {self._current_team.color.name}")
        for row in range(NUM_OF_ROWS):
            print()
            for col in range(NUM_OF_COLS):
                piece = self._board[row][col] if self._board[row][col] else "--"
                print("| " + str(piece) + " |", end="")

    def _calculate_piece_moves(self, piece: Piece) -> Set[Tuple[int, int]]:
        """Get the valid moves and captures of a given piece.

        This method finds all the valid moves and captures of a piece given its current coordinates.
        This method accounts for the location of friendly and enemy pieces for moves and captures.
        However, this method does not account for possibly moving the king into an attacked square.

        Args:
            coordinates (Tuple[int, int]): The coordinates of the piece.

        Returns:
            Set[Tuple[int, int]]: The set of valid coordinates the piece can move to.
        """
        # determine valid moves, cannot move past a piece in a given direction
        moves = set()
        for direction in piece.get_possible_moves():
            for move in direction:
                if self._is_vacant(move):
                    moves.add(move)
                else:
                    break

        # determine valid captures, once you capture a piece in a given direction, cannot capture pieces afterwards
        captures = set()
        for direction in piece.get_possible_captures():
            for capture in direction:
                if str(piece) == "BP":
                    print(capture)
                if self._is_capture(piece, capture):
                    print(f"capture")
                    captures.add(capture)
                    break

        valid_moves = moves.union(captures)

        return valid_moves

    def is_attacked(self, team: Team, coordinates: Tuple[int, int]) -> bool:
        """Determines if the given coordinates are attacked by opposing team.

        Returns:
            bool: True if the given coordinates are attacked by opposing team. Otherwise, False.
        """
        for _, move in team.get_moves():
            if coordinates == move:
                return True
        return False

    def is_check(self, team: Team) -> bool:
        """Determines if current team is in check position.

        Returns:
            bool: True if the curret team is in check position. Otherwise, False
        """
        king_coordinates = team.get_king().coordinates
        enemy = self._black if team.color == Color.WHITE else self._white
        return self.is_attacked(enemy, king_coordinates)

    def is_checkmate(self) -> bool:
        """Determines if current team is in a checkmate position.

        Returns:
            bool: True if current team is in a checkmate position. Otherwise, False.
        """
        king = self._current_team.get_king()

        if not self.is_check():
            return False

        for piece, move in self._current_team.get_moves():
            self._move_piece(piece, move)
            if not self.is_check():
                return False
        return True
