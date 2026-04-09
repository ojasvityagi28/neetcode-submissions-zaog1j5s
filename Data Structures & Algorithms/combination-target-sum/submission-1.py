class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.targetsum = 0
        res , sol = [] , []
        def dfs(i):
            if self.targetsum == target:
                res.append(sol[:])
                return
            elif i== len(nums) or self.targetsum > target:
                return
            
            dfs(i+1)

            sol.append(nums[i])
            self.targetsum += nums[i]
            dfs(i)
            #after last return we start popping and decreasing the sum
            a = sol.pop()
            self.targetsum -= a

        dfs(0)
        return res
        