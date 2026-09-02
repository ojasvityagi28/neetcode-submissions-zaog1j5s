class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        match = 0
        count = {}
        length , res = float('inf') , ""
        l = 0
        countT = Counter(t)

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            if s[r] in countT and count[s[r]] == countT[s[r]]:
                match += 1

            while match == len(countT):
                if r - l + 1 < length :
                    length = r - l + 1
                    res = s[l: l + length]
                # if s[l] in count and count[s[l]] > 0:
                count[s[l]] -= 1
                if s[l] in countT and count[s[l]] < countT[s[l]]:
                    match -= 1
                l += 1
        return res
            


        