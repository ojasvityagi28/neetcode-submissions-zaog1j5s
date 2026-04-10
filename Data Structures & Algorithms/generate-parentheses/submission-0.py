class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        sol = []
        def dfs(opening , closing):
            if closing == 0:
                res.append("".join(sol))
                return
            if opening:
                sol.append(('('))
                dfs(opening - 1, closing)
                sol.pop()
            if closing and opening < closing:
                sol.append(')')
                dfs(opening , closing - 1)
                sol.pop()
        dfs(n , n)
        return res


        