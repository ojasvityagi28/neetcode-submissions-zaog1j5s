class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                a = nums[l]
                b = nums[r]
                
                if a + b > -nums[i]:
                    r -= 1
                elif a + b < -nums[i]:
                    l += 1
                else:
                    res.append([a , b , nums[i]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res
                



        