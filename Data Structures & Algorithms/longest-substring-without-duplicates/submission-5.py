class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_index = {}
        res = 0
        l= r = 0
        for r in range(len(s)):
            if s[r] in seen_index and seen_index[s[r]] >= l:
                l = seen_index[s[r]] + 1
            seen_index[s[r]] = r
            res = max(res , r - l + 1)
        return res

