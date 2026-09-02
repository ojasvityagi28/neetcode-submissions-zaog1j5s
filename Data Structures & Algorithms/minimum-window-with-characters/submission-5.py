class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        count = Counter(t)
        l = 0
        matches = 0
        reslen , start = float('inf') , 0

        for r in range(len(s)):
            #expanding window
            if s[r] in count:
                count[s[r]] -= 1  
                if count[s[r]] >= 0:
                    matches += 1 

            #shrinking window
            while matches == len(t):
                if r - l + 1 < reslen:
                    start = l
                    reslen = r - l + 1
                if s[l] in count:
                    count[s[l]] += 1
                    if count[s[l]] > 0:
                        matches -=1
                l += 1 
        return s[start : start + reslen] if reslen != float('inf') else ""  