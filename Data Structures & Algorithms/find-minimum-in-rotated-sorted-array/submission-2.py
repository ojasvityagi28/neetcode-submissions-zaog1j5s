class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minimum = nums[0]
        while l <=r:
            mid = (l + r)//2
            if nums[mid] >= nums[0]:
                l = mid + 1
            else: 
                # we're in the right half ie the beginning
                minimum = nums[mid]
                r = mid - 1
        return minimum



        