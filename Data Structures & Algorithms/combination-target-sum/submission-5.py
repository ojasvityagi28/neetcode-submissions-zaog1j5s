class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res , sol = [] , []
        def dfs(i , total):
            if total == target:
                res.append(sol[:])
                return
            elif i== len(nums):
                return
            
            dfs(i+1 , total)

            if total + nums[i] > target:
                return
            sol.append(nums[i])
            total += nums[i]
            dfs(i , total)
            #after last return we start popping and decreasing the sum
            a = sol.pop()
            total -= a

        dfs(0 , 0)
        return res
        