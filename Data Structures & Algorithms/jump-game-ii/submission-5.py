class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = 0 #0th level starts at index 0
        res = 0
        farthest = 0

        while r < len(nums) - 1:
            for i in range(l , r + 1):
                farthest = max(farthest , i + nums[i])
            l = r + 1 #next level starts here
            r = farthest
            res += 1
        return res