class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        res = 0
        l = 0
        max_freq = 0

        for r in range(len(s)):
            # Expanding
            if s[r] not in freq:
                freq[s[r]] = 0

            freq[s[r]] += 1
            max_freq = max(max_freq, freq[s[r]])

            # Shrinking
            while (r - l + 1) - max_freq > k:
                freq[s[l]] -= 1
                l += 1

                # Recalculate max frequency after shrinking
                max_freq = 0
                for char in freq:
                    max_freq = max(max_freq, freq[char])

            res = max(res, r - l + 1)

        return res
        