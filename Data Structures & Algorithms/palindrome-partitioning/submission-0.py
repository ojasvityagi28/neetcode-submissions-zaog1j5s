class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def palindrome(abc : str):
            l = 0 
            r = len(abc)-1
            while l < r:
                if abc[l] != abc[r]:
                    return False
                l+=1
                r-=1
            return True

        res , sol = [] , []
        def dfs(start):
            if start == len(s):
                res.append(sol[:])
                return

            for i in range(start , len(s)):
                substring = s[start : i+1]
                if palindrome(substring):
                    sol.append(substring)
                    dfs(i + 1)
                    sol.pop()
        dfs(0)
        return res
           
                