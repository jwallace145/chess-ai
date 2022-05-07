from src.constants import NUM_OF_COLS, NUM_OF_ROWS

# unbounded moves (all directions)
MOVE_UP = [(-r, 0) for r in range(1, NUM_OF_ROWS)]
MOVE_DOWN = [(r, 0) for r in range(1, NUM_OF_ROWS)]
MOVE_LEFT = [(0, -c) for c in range(1, NUM_OF_COLS)]
MOVE_RIGHT = [(0, c) for c in range(1, NUM_OF_COLS)]
MOVE_UP_RIGHT_DIAGONALLY = [(i, i) for i in range(1, NUM_OF_ROWS)]
MOVE_UP_LEFT_DIAGONALLY = [(i, -i) for i in range(1, NUM_OF_ROWS)]
MOVE_DOWN_RIGHT_DIAGONALLY = [(-i, -i) for i in range(1, NUM_OF_ROWS)]
MOVE_DOWN_LEFT_DIAGONALLY = [(-i, i) for i in range(1, NUM_OF_ROWS)]


# moves of length one (all directions)
MOVE_UP_ONE = [(-1, 0)]
MOVE_DOWN_ONE = [(1, 0)]
MOVE_LEFT_ONE = [(0, -1)]
MOVE_RIGHT_ONE = [(0, 1)]
MOVE_UP_RIGHT_DIAGONALLY_ONE = [(-1, 1)]
MOVE_UP_LEFT_DIAGONALLY_ONE = [(-1, -1)]
MOVE_DOWN_RIGHT_DIAGONALLY_ONE = [(1, 1)]
MOVE_DOWN_LEFT_DIAGONALLY_ONE = [(1, -1)]


# moves of length two (only valid in up/down directions)
MOVE_UP_TWO = [(-2, 0)]
MOVE_DOWN_TWO = [(2, 0)]


# knight moves
MOVE_UP_TWO_LEFT_ONE = [(-2, -1)]
MOVE_UP_TWO_RIGHT_ONE = [(-2, 1)]
MOVE_DOWN_TWO_LEFT_ONE = [(2, -1)]
MOVE_DOWN_TWO_RIGHT_ONE = [(2, 1)]
MOVE_LEFT_TWO_UP_ONE = [(-1, -2)]
MOVE_LEFT_TWO_DOWN_ONE = [(1, -2)]
MOVE_RIGHT_TWO_UP_ONE = [(-1, 2)]
MOVE_RIGHT_TWO_DOWN_ONE = [(1, 2)]
