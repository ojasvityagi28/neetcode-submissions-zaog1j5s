class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        reslen = 0
        def palindrome(l , r ):
            nonlocal reslen, start
            while l >= 0  and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > reslen:
                    reslen = r - l + 1
                    start = l
                l-=1
                r+=1

        for i in range(len(s)):
            
            palindrome(i , i)
            
            palindrome(i , i + 1 )


        return s[start : start + reslen]
            


        