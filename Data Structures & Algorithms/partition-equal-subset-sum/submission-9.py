class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums)//2
        dp = {}

        def dfs( i , target):
            if target == 0:
                return True
            if (target , i) in dp:
                return dp[(target, i)]

            if i == len(nums):
                return False

            take = False
            if nums[i] <= target:
                take = dfs( i + 1 , target - nums[i])

            skip =dfs(i + 1 , target)
            dp[(target, i)] = take or skip

            return dp[(target , i)]
        return dfs(0 , target)




        