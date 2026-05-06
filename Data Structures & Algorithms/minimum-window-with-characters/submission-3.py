class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        match = len(t)
        count = Counter(t)
        size = float('inf')
        i = 0
        start , end = 0 , 0
        
        for j in range(len(s)):
            #expand window
            if s[j] in count:
                count[s[j]] -= 1
                if count[s[j]] >= 0:
                    match -= 1
            #shrink window
            while match == 0:
                if j - i + 1 < size:
                    size = j - i + 1
                    start = i
                    end = j + 1

                if s[i] in count:
                    count[s[i]] += 1
                    if count[s[i]] > 0:
                        match += 1
                i += 1

        res = s[start : end]
        return res
