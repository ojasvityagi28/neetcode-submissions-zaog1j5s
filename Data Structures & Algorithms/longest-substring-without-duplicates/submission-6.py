class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        charMap = {}
        res = 0

        for r in range(len(s)):
            if s[r] in charMap and charMap[s[r]] >= l:
                l = charMap[s[r]] + 1
                
            charMap[s[r]] = r
            res = max(res , r - l + 1)
        return res
        