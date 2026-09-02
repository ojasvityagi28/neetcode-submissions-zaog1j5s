class Solution:
    def climbStairs(self, n: int) -> int:
        two = 1 #no. of ways to reach the (i - 2)th step
        one = 1#no. of ways to reach the (i - 1)th step

        for a in range(2, n + 1):
            tmp = one
            one = one + two
            two = tmp
        return one