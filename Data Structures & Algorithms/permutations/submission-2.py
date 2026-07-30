class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sol = []
        seen = set()
        res = []

        def dfs():
            if len(sol) == len(nums):
                res.append(sol[:])
                return
            
            for i in range(len(nums)):
                if nums[i] in seen:
                    continue
                sol.append(nums[i])
                seen.add(nums[i])
                dfs()
                sol.pop()
                seen.remove(nums[i])
        dfs()
        return res

        