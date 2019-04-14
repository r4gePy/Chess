WHITE = 1

BLACK = 2


def opponent(color):
    if color == WHITE:
        return BLACK
    else:
        return WHITE


color = WHITE
if color == BLACK:
    # do_something()
    pass

opponent_color = opponent(color)


def print_board(board):
    print('     +----+----+----+----+----+----+----+----+')
    for row in range(7, -1, -1):
        print(' ', row, end=' ')
        for col in range(8):
            print("|", board.cell(row, col), end=' ')
        print("|")
        print("     +----+----+----+----+----+----+----+----+")
    print(end='      ')
    for col in range(8):
        print(col, end='      ')
    print()


def main():
    board = Board()
    while True:
        print_board(board)
        print("Команды:")
        print("      exit                                  -- выход")
        print("      move <row> <col> <row1> <col1>        -- ход из"
              "клетки (row, col)")
        print("                                                в"
              "клетку (row1, col1)")
        if board.current_player_color() == WHITE:
            print("Ход белых:")
        else:
            print("Ход чёрных:")
        command = input()
        if command == "exit":
            break
        move_type, row, col, row1, col1 = command.split()
        row, col, row1, col = int(row), int(col), int(row1), int(col1)
        if board.move_piece(row, col, row1, col1):
            print("Ход успешен")
        else:
            print("Координаты некорректны! Попробуйте другой ход!")


def correct_coords(row, col):
    return 0 <= row < 8 and 0 <= col < 8


class Board:
    def __init__(self):
        self.color = WHITE
        self.field = []
        for row in range(8):
            self.field.append([None] * 8)
        self.field[1][4] = Pawn(1, 4, WHITE)

    def current_player_color(self):
        return self.color

    def cell(self, row, col):
        piece = self.field[row][col]
        if piece is None:
            return "  "
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()


    def move_piece(self, row, col ,row1, col1):
        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False
        if not piece.can_move(row1, col1):
            return False
        self.field[row][col] = None
        self.field[row1][col1] = piece
        piece.set_position(row1, col1)
        self.color = opponent(self.color)
        return True


class Pawn:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return "P"

    def get_color(self):
        return self.color

    def can_move(self, row, col):
        if self.color != col:
            return False
        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6
        if self.row + direction == row:
            return True
        if self.row == start_row and self.row + 2 * direction == row:
            return True
        return False


class Rook:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return "R"

    def get_color(self):
        return self.color

    def can_move(self, row, col):
        if self.row != row and self.col != col:
            return False
        return True