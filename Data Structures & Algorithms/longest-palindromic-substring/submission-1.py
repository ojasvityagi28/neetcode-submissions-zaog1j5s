class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        reslen = 0
        def palindrome(l , r ):
            nonlocal res , reslen
            while l >= 0  and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > reslen:
                    reslen = r - l + 1
                    res = s[l : l + reslen]
                l-=1
                r+=1
            return res

        for i in range(len(s)):
            
            palindrome(i , i)
            
            palindrome(i , i + 1 )


        return res
            


        