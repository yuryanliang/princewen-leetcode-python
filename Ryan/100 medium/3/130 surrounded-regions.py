"""

"""


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        Modify the dfs used in Number of Island.
Using DFS to traverse the boundaries, when 'O' is found, fire the dfs() to flip all the connected 'O' into ' * '.
After that, go through the board and flip the other 'O' to 'X', since these 'O' cannot escape the board. Then flip all the '*' to 'O', indicating these 'O' can reach out of the board.
        """
        if not board:
            return

        m = len(board)
        n = len(board[0])
        if m > 2 or n > 2:

            m = len(board)
            n = len(board[0])

            for i in range(m - 1):
                if board[i][0] == "O":
                    self.dfs(i, 1, board)
                if board[i][n - 1] == "O":
                    self.dfs(i, n - 2, board)

            for j in range(n - 1):
                if board[m - 1][j] == "O":
                    self.dfs(m - 2, j, board)
                if board[0][j] == "O":
                    self.dfs(1, j, board)

            for i in range(1, m - 1):
                for j in range(1, n - 1):
                    if board[i][j] == "O":
                        board[i][j] = "X"
                    elif board[i][j] == "A":
                        board[i][j] = "O"

    def dfs(self, i, j, board):
        # hit boundary or "X"
        if i <= 0 or j <= 0 or i >= len(board) - 1 or j >= len(board[0]) - 1 or board[i][j] == "X":
            return

        # hit other "A"
        if board[i][j] == "A":
            return

        if board[i][j] == "O":
            board[i][j] = "A"

        self.dfs(i + 1, j, board)
        self.dfs(i - 1, j, board)
        self.dfs(i, j + 1, board)
        self.dfs(i, j - 1, board)
if __name__ == "__main__":
    board = [['X', 'X', 'X', 'X'],
             ['X', 'O', 'O', 'X'],
             ['X', 'X', 'O', 'X'],
             ['X', 'O', 'X', 'X']]
    Solution().solve(board)
    print (board)