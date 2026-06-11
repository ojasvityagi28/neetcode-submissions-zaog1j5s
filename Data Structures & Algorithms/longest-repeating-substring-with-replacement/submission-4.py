class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_count = {}
        l = r = 0
        res = 0
        for r in range(len(s)):
            if s[r] not in max_count:
                max_count[s[r]] = 0
            max_count[s[r]] += 1
            window = r - l + 1
            to_be_replaced = window - max(max_count.values())
            if to_be_replaced > k:
                max_count[s[l]] -= 1
                l += 1
            res = max(res , r - l + 1)
        return res


        