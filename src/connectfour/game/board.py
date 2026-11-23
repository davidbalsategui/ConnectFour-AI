
ROWS = 6
COLS = 7


class Board:

    def __init__(self):
        self.grid = [
            [0 for _ in range(COLS)]
            for _ in range(ROWS)
        ]

    def is_valid_move(self, col: int) -> bool:
        return COLS > col >= 0 == self.grid[0][col]

    def get_valid_moves(self) -> list[int]:
        return [
            col for col in range(COLS)
            if self.is_valid_move(col)
        ]

    def drop_piece(self, col: int, player: int) -> int:
        if player not in (1, -1):
            raise ValueError("Invalid player")

        if not self.is_valid_move(col):
            raise ValueError("Invalid or full column")

        for row in range(ROWS - 1, -1, -1):
            if self.grid[row][col] == 0:
                self.grid[row][col] = player
                return row

        raise RuntimeError("Unexpected board state")

    def is_full(self) -> bool:
        return len(self.get_valid_moves()) == 0

    def copy(self) -> "Board":
        new_board = Board()
        new_board.grid = [row.copy() for row in self.grid]
        return new_board

    def display(self) -> None:
        symbols = {
            0: ".",
            1: "X",
            -1: "O"
        }

        for row in self.grid:
            print(" ".join(symbols[cell] for cell in row))

        print("0 1 2 3 4 5 6")
