class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_count = {}
        max_f = 0
        l = r = 0
        res = 0
        for r in range(len(s)):
            if s[r] not in max_count:
                max_count[s[r]] = 0
            max_count[s[r]] += 1
            max_f = max(max_f , max_count[s[r]])
            window = r - l + 1
            to_be_replaced = window - max_f
            if to_be_replaced > k:
                max_count[s[l]] -= 1
                l += 1
            res = max(res , r - l + 1)
        return res


        