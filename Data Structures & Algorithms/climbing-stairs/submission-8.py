class Solution:
    def climbStairs(self, n: int) -> int:
        two = 1
        one = 1

        for a in range(n - 2, -1 , -1):
            tmp = one
            one = one + two
            two = tmp
        return one