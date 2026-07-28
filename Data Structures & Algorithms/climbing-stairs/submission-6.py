class Solution:
    def climbStairs(self, n: int) -> int:
        oneStep = 1
        twoSteps = 1
        for i in range(n - 2 , -1 , -1):
            tmp = oneStep
            oneStep = oneStep + twoSteps
            twoSteps = tmp
        return oneStep


        