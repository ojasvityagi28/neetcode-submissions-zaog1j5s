class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if nums[0] == target:
            return True

        l , r = 0 , len(nums) - 1
        while r > 0 and nums[r] == nums[0]:
            r -= 1
        
        while l <= r:
            mid = (l + r)//2

            if nums[mid] == target:
                return True

            elif nums[mid] >= nums[0]: #second half
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False

        
        