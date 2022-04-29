from src.board import Board

board = Board()

board.print_board()

print()

print(f"black king valid moves: {board.get_valid_moves((0, 4))}")

board.move_piece((1, 4), (2, 4))

board.print_board()

print()

print(f"black king valid moves: {board.get_valid_moves((0, 4))}")

board.move_piece((0, 4), (1, 4))

board.print_board()

print()

print(f"black king valid moves: {board.get_valid_moves((1, 4))}")
