class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        res = 0
        l = 0
        max_freq = 0

        for r in range(len(s)):
            if s[r] not in freq:
                freq[s[r]] = 0
            freq[s[r]] += 1

            if freq[s[r]] > max_freq:
                max_freq = freq[s[r]]

            while (r - l + 1) - max_freq > k:
                freq[s[l]] -= 1
                #no need to check for max_freq again as we have only decremented
                l += 1
            res = max(res , r - l + 1)
        return res
