class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res , sol = [] , []

        def dfs(i):
            if i == len(nums):
                res.append(sol[:])
                return
            j = i
            while j + 1 < len(nums) and nums[j + 1] == nums[j]:
                j+=1
            dfs(j+1)# dont pick it

            sol.append(nums[i])
            dfs(i+1) # pick it the again do the same process of not picking and picking numbers ahead
            sol.pop()
        dfs(0)
        return res

        