class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sol = []
        res = []

        def dfs(opening , closing):
            if opening == closing == 0:
                res.append("".join(sol))
                return
            if opening > 0:
                sol.append("(")
                dfs(opening - 1, closing)
                sol.pop()
            if opening < closing:
                sol.append(")")
                dfs(opening , closing - 1)
                sol.pop()
        dfs(n , n)
        return res

        