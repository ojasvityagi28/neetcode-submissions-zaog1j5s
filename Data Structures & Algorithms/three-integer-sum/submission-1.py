class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for a in range(len(nums)-2):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            l = a+1
            r = len(nums)-1
            while l < r:
                if nums[a] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[a] + nums[l] + nums[r] < 0:
                    l +=1
                else:
                    res.append([nums[a],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                    while l < r and nums[r] == nums[r+1]:
                        r-=1

        return res


        