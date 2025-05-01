# Assignment-B4 (N-Queen with Branch and Bound and Backtracking)

class NQBranchAndBond:
    def printSolution(self, board):
        print("\nN Queen Branch and Bound Solution:")
        for row in board:
            print(" ".join(['Q' if cell else '.' for cell in row]))

    def isSafe(self, row, col, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup):
        return not (slashCodeLookup[slashCode[row][col]] or
                    backslashCodeLookup[backslashCode[row][col]] or
                    rowLookup[row])

    def solveNQUtil(self, board, col, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup, N):
        if col >= N:
            return True

        for i in range(N):
            if self.isSafe(i, col, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup):
                board[i][col] = 1
                rowLookup[i] = True
                slashCodeLookup[slashCode[i][col]] = True
                backslashCodeLookup[backslashCode[i][col]] = True

                if self.solveNQUtil(board, col + 1, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup, N):
                    return True

                board[i][col] = 0
                rowLookup[i] = False
                slashCodeLookup[slashCode[i][col]] = False
                backslashCodeLookup[backslashCode[i][col]] = False

        return False

    def solveNQ(self, N):
        board = [[0 for _ in range(N)] for _ in range(N)]
        slashCode = [[0 for _ in range(N)] for _ in range(N)]
        backslashCode = [[0 for _ in range(N)] for _ in range(N)]
        rowLookup = [False] * N
        slashCodeLookup = [False] * (2 * N - 1)
        backslashCodeLookup = [False] * (2 * N - 1)

        for i in range(N):
            for j in range(N):
                slashCode[i][j] = i + j
                backslashCode[i][j] = i - j + N - 1

        if not self.solveNQUtil(board, 0, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup, N):
            print("\nNo solution exists for Branch and Bound.")
            return

        self.printSolution(board)


class NQBacktracking:
    def __init__(self):
        self.ld = [0] * 30
        self.rd = [0] * 30
        self.cl = [0] * 30

    def printSolution(self, board):
        print("\nN Queen Backtracking Solution:")
        for row in board:
            print(" ".join(['Q' if cell else '.' for cell in row]))

    def solveNQUtil(self, board, col, N):
        if col >= N:
            return True

        for i in range(N):
            if self.ld[i - col + N - 1] == 0 and self.rd[i + col] == 0 and self.cl[i] == 0:
                board[i][col] = 1
                self.ld[i - col + N - 1] = self.rd[i + col] = self.cl[i] = 1

                if self.solveNQUtil(board, col + 1, N):
                    return True

                board[i][col] = 0
                self.ld[i - col + N - 1] = self.rd[i + col] = self.cl[i] = 0

        return False

    def solveNQ(self, N):
        board = [[0 for _ in range(N)] for _ in range(N)]
        if not self.solveNQUtil(board, 0, N):
            print("\nNo solution exists for Backtracking.")
            return
        self.printSolution(board)


if __name__ == "__main__":
    N = int(input("Enter the number of queens: "))

    bab = NQBranchAndBond()
    bab.solveNQ(N)

    bt = NQBacktracking()
    bt.solveNQ(N)
