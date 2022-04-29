from src.board import Board

board = Board()

board.print_board()

print()

print(f"black rook valid moves: {board.get_valid_moves((0, 0))}")

board.move_piece((1, 0), (2, 0))

board.print_board()

print()

print(f"black rook valid moves: {board.get_valid_moves((0, 0))}")

board.move_piece((2, 0), (3, 0))

board.print_board()

print()

print(f"black rook valid moves: {board.get_valid_moves((0, 0))}")

board.move_piece((0, 0), (2, 0))

board.print_board()

print()

print(f"black rook valid moves: {board.get_valid_moves((2, 0))}")

board.move_piece((2, 0), (2, 4))

board.print_board()

print()

print(f"black rook valid moves: {board.get_valid_moves((2, 4))}")
