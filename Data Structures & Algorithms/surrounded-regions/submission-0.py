class Solution:
    def solve(self, board):
        rows, cols = len(board), len(board[0])

        def dfs(i, j, visited, region):
            # out of bounds → not surrounded
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return False

            if board[i][j] == "X":
                return True

            if (i, j) in visited:
                return True  # already processed in this region

            visited.add((i, j))
            region.append((i, j))

            up = dfs(i + 1, j, visited, region)
            down = dfs(i - 1, j, visited, region)
            left = dfs(i, j - 1, visited, region)
            right = dfs(i, j + 1, visited, region)

            return up and down and left and right

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    visited = set()
                    region = []

                    if dfs(r, c, visited, region):
                        for i, j in region:
                            board[i][j] = "X"