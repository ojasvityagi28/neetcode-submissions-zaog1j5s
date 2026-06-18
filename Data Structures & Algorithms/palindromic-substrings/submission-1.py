class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0
        for i in range(len(s)):
            odd_count = self.palindrome(s , i , i)
            even_count = self.palindrome(s , i , i + 1)
            total += odd_count + even_count
        return total
    
    def palindrome(self , s , l , r):
        count = 0
        while l>=0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -=1
            r += 1
        return count

        