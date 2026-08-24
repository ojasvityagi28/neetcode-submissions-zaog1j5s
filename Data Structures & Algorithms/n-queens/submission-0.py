class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        forward = set()
        backward = set()

        res = []
        board = [["."]*n for _ in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in cols or (r - c) in forward or (r + c) in backward:
                    continue
                
                board[r][c] = "Q"
                cols.add(c)
                forward.add((r - c))
                backward.add((r + c))

                backtrack(r + 1)

                board[r][c] = "."
                cols.remove(c)
                forward.remove((r - c))
                backward.remove((r + c))

        backtrack(0)
        return res
