# game state

class Board:
    def __init__(self):
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.print_board()

    def print_board(self):
        for i in range(3):
            print(f" {self.board[0 + 3 * i]} | {self.board[1 + 3 * i]} | {self.board[2 + 3 * i]} ")
            if i < 2:
                print("-----------")
        print()

    def check_cols(self, char):
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] == char:
                return True
        return False

    def check_rows(self, char):
        for i in range(3):
            if self.board[3 * i] == self.board[3 * i + 1] == self.board[3 * i + 2] == char:
                return True
        return False

    def check_diag(self, char):
        if self.board[0] == self.board[4] == self.board[8] == char or self.board[2] == self.board[4] == self.board[6] == char:
            return True
        return False

    def check_board(self, char):
        if self.check_cols(char) or self.check_rows(char) or self.check_diag(char):
            return "Win"
        elif all(char != " " for char in self.board):
            return "Draw"
        else:
            return "Continue"
    def update(self, x, y, char):
        self.board[3 * y + x] = char

    def reset(self):
        for i in range(9):
            self.board[i] = " "

    def char_at(self, x, y):
        return self.board[3 * y + x]

