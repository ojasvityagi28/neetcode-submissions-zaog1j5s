class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()

        def dfs(sol):
            if len(sol) == len(nums):
                res.append(sol[:])
                return
            for i in range(len(nums)):
                if nums[i] in seen:
                    continue
                sol.append(nums[i])
                seen.add(nums[i])
                dfs(sol) #choose
                seen.remove(nums[i])
                sol.pop()
        dfs([])
        return res
