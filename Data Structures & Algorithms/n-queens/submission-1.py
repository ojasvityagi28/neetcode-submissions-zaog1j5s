class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        forward = set()
        reverse = set()
        res = []
        sol = [["."]*n for _ in range(n)]


        def backtracking(r):
            if r == n:
                res.append(["".join(row) for row in sol])
                return 
            
            for c in range(n):
                if c in cols or (r - c) in forward or (r + c) in reverse:
                    continue
                
                sol[r][c] = "Q"
                cols.add(c)
                forward.add((r - c))
                reverse.add((r + c))

                backtracking(r + 1)

                cols.remove(c)
                forward.remove((r - c))
                reverse.remove((r + c))
                sol[r][c] = "."
        
        backtracking(0)
        return res
            



            
                



        