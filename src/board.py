from dataclasses import dataclass, field
from typing import List, Literal, Set, Tuple

from src.constants import NUM_OF_COLS, NUM_OF_ROWS, Color, PieceEnum
from src.exceptions import InvalidMove
from src.pieces.king import King
from src.pieces.piece import Piece
from src.teams.black import Black
from src.teams.team import Team
from src.teams.white import White


@dataclass
class Board:

    _black: Team = Black()
    _white: Team = White()
    _board: List[List[str]] = field(
        default_factory=lambda: [
            [None for _ in range(NUM_OF_COLS)] for _ in range(NUM_OF_ROWS)
        ]
    )

    def initialize(
        self,
        black: Black = None,
        white: White = None,
        current_team: Team = None,
        opposing_team: Team = None,
    ) -> None:
        # initialize starting pieces
        if not black and not white:
            self._current_team = self._white
            self._opposing_team = self._black
            self._black.initialize()
            self._white.initialize()
        else:
            self._current_team = current_team
            self._opposing_team = opposing_team
            self._black = black
            self._white = white

        pieces = self._black.get_all_pieces().union(self._white.get_all_pieces())
        for piece in pieces:
            self._place_piece(piece, piece.coordinates)

    def move_piece(self, src: Tuple[int, int], dest: Tuple[int, int]) -> None:
        """Move chess piece to valid destination.

        Args:
            src (Tuple[int, int]): The coordinates of the chess piece.
            dest (Tuple[int, int]): The coordinates of the desitination.

        Raises:
            InvalidMove: Raise an InvalidMove exception if the move is not valid.
        """
        if dest in self.get_moves(src):
            piece = self._pickup_piece(src)
            piece.has_moved = True
            self._place_piece(piece, dest)
            self._current_team, self._opposing_team = (
                self._opposing_team,
                self._current_team,
            )
        else:
            raise InvalidMove(dest)

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

    def _is_capture(self, piece: Piece, coordinates: Tuple[int, int]) -> bool:
        """Determine if moving the piece to the given destination cell is an enemy capture.

        Args:
            piece (Piece): The given chess piece.
            coordinates (Tuple[int, int]): The destination coordinates of possible enemy capture.

        Returns:
            bool: True if moving the given piece to the destination coordinates captures an enemy piece. Otherwise, False
        """
        enemy = self._get_piece(coordinates)
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

    def _pickup_piece(self, coordinates: Tuple[int, int]) -> Piece:
        """Pick up and remove chess piece from given coordinates and return the chess piece.

        Args:
            coordinates (Tuple[int, int]): The coordinates of the chess piece.

        Returns:
            Piece: The chess piece at the given coordinates.
        """
        row, col = coordinates
        piece = self._board[row][col]
        self._board[row][col] = None
        return piece

    def _place_piece(self, piece: Piece, coordinates: Tuple[int, int]) -> None:
        """Place chess piece at the given coordinates.

        Args:
            piece (Piece): The chess piece.
            coordinates (Tuple[int, int]): The desired coordinates.
        """
        piece.coordinates = coordinates
        row, col = coordinates
        self._board[row][col] = piece

    def find_piece(self, piece: PieceEnum, dest_coordinates: Tuple[int, int]) -> Piece:
        """Find chess piece given the type of chess piece and destination coordinates.

        This method is helpful for finding the desired chess piece given a move in the
        syntax "P E4". This means move current team Pawn to square E4 (4,4).

        Args:
            piece (PieceEnum): The type of chess piece
            dest_coordinates (Tuple[int, int]): The destination coordinates of the given chess piece.

        Raises:
            InvalidMove: Raises an InvalidMove exception if none of the current team pieces can move to the
                         given destination square.

        Returns:
            Piece: The chess piece that can make to the given destination square.
        """
        pieces = self._current_team.get_pieces(piece)

        possible_pieces = []
        for piece in pieces:
            if dest_coordinates in self._get_valid_moves_and_captures(
                piece.coordinates
            ):
                possible_pieces.append(piece)

        if len(possible_pieces) == 0:
            raise InvalidMove(dest_coordinates)
        elif len(possible_pieces) == 1:
            return possible_pieces[0]
        else:
            print("MULTIPLE PIECES FOUND NOT GOOD")
            return possible_pieces[0]

    def _get_valid_moves_and_captures(
        self, coordinates: Tuple[int, int]
    ) -> Set[Tuple[int, int]]:
        """Get the valid moves and captures of a given piece.

        This method finds all the valid moves and captures of a piece given its current coordinates.
        This method accounts for the location of friendly and enemy pieces for moves and captures.
        However, this method does not account for possibly moving the king into an attacked square.

        Args:
            coordinates (Tuple[int, int]): The coordinates of the piece.

        Returns:
            Set[Tuple[int, int]]: The set of valid coordinates the piece can move to.
        """
        piece = self._get_piece(coordinates)

        valid_moves = set()
        for direction in piece.get_possible_moves():
            for move in direction:
                if self._is_vacant(move):
                    valid_moves.add(move)
                else:
                    break

        valid_captures = set()
        for direction in piece.get_possible_captures():
            for move in direction:
                if not self._is_vacant(move) and self._is_capture(piece, move):
                    valid_captures.add(move)
                    break

        return valid_moves.union(valid_captures)

    def get_moves(self, coordinates: Tuple[int, int]) -> Set[Tuple[int, int]]:
        """Get the moves of a piece at the given coordinates.

        This method returns the set of valid moves and captures. This method accounts
        for a King piece that cannot move into an attacked square.

        Args:
            coordinates (Tuple[int, int]): The coordinates of the given piece

        Returns:
            Set[Tuple[int, int]]: The set of valid moves and captures. Including the King parity.
        """
        moves = self._get_valid_moves_and_captures(coordinates)

        # if the piece is a king, remove any possible move/capture that is attacked
        piece = self._get_piece(coordinates)
        if isinstance(piece, King):
            moves = [move for move in moves if not self.is_under_attack(move)]

        return moves

    def get_valid_castles(self) -> bool:
        # check king has not moved
        # check at least one of rooks have not moved
        # check spaces between rook(s) and king are vacant
        # check king is not in check
        # check path king takes to castle does not put king in check
        # return True if all the above is satisfied
        king = self._current_team.get_king()
        rooks = self._current_team.get_pieces(PieceEnum.ROOK)

        # check if king has moved
        if king.has_moved:
            return []

        # check if rook(s) exist that have not moved
        rooks = [rook for rook in rooks if not rook.has_moved]
        if len(rooks) == 0:
            return []

        # check vacant path to rooks
        clear_path_to_rooks = []
        for rook in rooks:
            k_row, k_col = king.coordinates
            r_row, r_col = rook.coordinates
            if k_col > r_col:  # king is to right of rook
                new_col = k_col - 1
                while new_col != r_col:
                    if not self._is_vacant((k_row, new_col)):
                        break
                    new_col -= 1
                if new_col == r_col:
                    clear_path_to_rooks.append(rook)
            elif k_col < r_col:  # king is to left of rook
                new_col = k_col + 1
                while new_col != r_col:
                    if not self._is_vacant((k_row, new_col)):
                        break
                    new_col += 1
                if new_col == r_col:
                    clear_path_to_rooks.append(rook)
        if len(clear_path_to_rooks) == 0:
            return []

        # check if king is under attack
        if self.is_under_attack(king.coordinates):
            return []

        possible_castles = []
        for rook in clear_path_to_rooks:
            k_row, k_col = king.coordinates
            r_row, r_col = rook.coordinates
            if k_col > r_col:  # move king two spaces to left
                for i in range(2):
                    try:
                        self.move_piece(king.coordinates, (k_row, k_col - i - 1))
                    except InvalidMove:
                        break
                if king.coordinates == (k_row, k_col - 2):
                    possible_castles.append(rook)
                    self.move_piece(king.coordinates, (k_row, k_col))
            elif k_col < r_col:  # move king two spaces to right
                for i in range(2):
                    try:
                        self.move_piece(king.coordinates, (k_row, k_col + i + 1))
                    except InvalidMove:
                        break
                if king.coordinates == (k_row, k_col + 2):
                    possible_castles.append(rook)
                    self._place_piece(king, (k_row, k_col))

        return possible_castles

    def is_under_attack(self, coordinates: Tuple[int, int]) -> bool:
        """Determines if current team is in a check position.

        Returns:
            bool: True if current team is in a check position. Otherwise, False.
        """
        enemy_pieces = self._opposing_team.get_all_pieces()

        enemy_valid_moves = set()
        for enemy in enemy_pieces:
            enemy_valid_moves.update(
                self._get_valid_moves_and_captures(enemy.coordinates)
            )

        if coordinates in enemy_valid_moves:
            return True
        return False

    def is_checkmate(self) -> bool:
        """Determines if current team is in a checkmate position.

        Returns:
            bool: True if current team is in a checkmate position. Otherwise, False.
        """
        king = self._current_team.get_king()

        if not self.is_under_attack(king.coordinates):
            return False

        enemy_pieces = self._opposing_team.get_all_pieces()

        king_moves = self.get_moves(king.coordinates)

        enemy_valid_moves = set()
        for enemy in enemy_pieces:
            enemy_valid_moves.update(self.get_moves(enemy.coordinates))

        for move in king_moves:
            if move not in enemy_valid_moves:
                return False
        return True
