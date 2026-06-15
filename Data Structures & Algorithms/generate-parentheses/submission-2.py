class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        openP = closeP= n
        res = []

        def dfs(openP, closeP , para_str):
            if openP == closeP == 0:
                res.append(para_str)
                return
            if openP == closeP:
                dfs(openP - 1 , closeP ,  para_str + "(")
            elif openP < closeP:
                if openP > 0:
                    dfs(openP - 1, closeP , para_str + "(")
                dfs(openP , closeP - 1 ,  para_str + ")")
        dfs(n , n , "")
        return res
            

        