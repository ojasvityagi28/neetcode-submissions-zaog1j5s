class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarysearch(l , r):
            while l <= r:
                mid = (l + r)//2
                if nums[mid] == target:
                    return mid
                elif target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1

        if nums[-1] > nums[0]:
            return binarysearch(0 , len(nums) - 1)

        l , r = 0 , len(nums) - 1
        pivot = 0
        while l <= r:
            index = (l + r)//2

            if nums[index] >= nums[0]:
                l = index + 1
            else:
                pivot = index
                r = index - 1

        if target >= nums[pivot] and target <= nums[-1]:
            return binarysearch(pivot , len(nums) - 1)

        elif target >= nums[0] and target <= nums[pivot - 1]:
            return binarysearch(0 , pivot - 1)

        else:
            return -1





        