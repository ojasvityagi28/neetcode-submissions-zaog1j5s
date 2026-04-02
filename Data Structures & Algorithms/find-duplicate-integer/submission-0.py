class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while nums[fast] and nums[nums[fast]]:# so we dont assign a null value and cause error
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

        