class Solution:
    def partition(self, s: str) -> List[List[str]]:
        sol = []
        res = []
        def isPali(s):
            l , r = 0 , len(s) - 1
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True

        def backtrack(start):
            if start == len(s):
                res.append(sol[:])
                return
            for i in range(start, len(s)):
                substring = s[start : i + 1]
                if isPali(substring):
                    sol.append(substring)
                    backtrack(i + 1)
                    sol.pop()
        backtrack(0)
        return res

        
        