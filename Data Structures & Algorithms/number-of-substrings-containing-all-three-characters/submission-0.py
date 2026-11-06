class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        start = 0
        l = 0
        res = 0
        count = {'a' : 0 , 'b' : 0 , 'c' : 0}

        for r in range(len(s)):
            count[s[r]] += 1
            while count['a'] >= 1 and count['b'] >= 1 and count['c'] >= 1:
                count[s[l]] -= 1
                l += 1
            res += l
        return res
