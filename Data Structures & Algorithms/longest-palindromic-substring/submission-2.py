class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.s = s
        self.reslen = 0
        self.residx = 0
        for i in range(len(s)):
            self.palindrome(i , i)
            self.palindrome(i , i + 1)

        return s[self.residx : self.residx + self.reslen]
    def palindrome(self ,l ,r):

        while l >= 0 and r < len(self.s) and self.s[l] == self.s[r]:
            if r - l + 1 > self.reslen:
                self.reslen = r - l + 1
                self.residx = l
            l-=1
            r+=1


        