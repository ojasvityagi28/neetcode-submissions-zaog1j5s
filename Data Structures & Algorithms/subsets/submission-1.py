class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        res = []
        def dfs(i):
            nonlocal res
            if i == len(nums):
                res.append(subset[:])
                return
            dfs(i + 1)

            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
        dfs(0)
        return res

        