class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indexMap = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in indexMap and indexMap[s[r]] >= l:
                l = indexMap[s[r]] + 1
            indexMap[s[r]] = r
            res = max(r - l + 1, res)
        return res
        