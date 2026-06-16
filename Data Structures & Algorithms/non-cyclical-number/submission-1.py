class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.sumOfSquares(n)

        while slow != fast:
            slow = self.sumOfSquares(slow)
            fast = self.sumOfSquares(self.sumOfSquares(fast))
        return True if slow == 1 else False
    
    def sumOfSquares(self ,n: int) -> int:
        total = 0
        while n:
            total += (n % 10)**2
            n = n//10
        return total



        