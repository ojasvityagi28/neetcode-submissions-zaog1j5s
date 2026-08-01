class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        def palindrome(l , r):
            while l >= 0 and r < len(s) and s[r] == s[l]:
                l -= 1
                r += 1

            return s[l + 1 : r ]
        
        for i in range(len(s)):

            string = palindrome(i , i)
            if len(string) > len(res):
                res = string


            string = palindrome(i , i + 1)
            if len(string) > len(res):
                res = string
        return res
            



        