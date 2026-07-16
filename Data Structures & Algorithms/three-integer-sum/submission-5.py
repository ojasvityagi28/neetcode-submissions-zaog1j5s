class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            a = nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:

                if a + nums[l] + nums[r] < 0:
                    l += 1
                elif a + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    res.append([a , nums[l] , nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res
                        