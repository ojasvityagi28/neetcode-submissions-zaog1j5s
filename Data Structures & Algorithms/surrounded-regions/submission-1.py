class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def dfs(i, j):
            if i < 0 or i == rows or j < 0 or j == cols or  board[i][j] != "O":
                return

            board[i][j] = "T"

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        for r in range(rows):
            if board[r][0] == "O":
                dfs(r , 0)
            if board[r][cols - 1] == "O":
                dfs(r , cols -1)

        for c in range(cols):
            if board[0][c] == "O":
                dfs(0 , c)
            if board[rows - 1][c] == "O":
                dfs(rows - 1 , c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"   
                elif board[r][c] == "T":
                    board[r][c] = "O"
                    
