class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = sorted(set(nums))  # Sort and remove duplicates
        length = 1
        maxlength = 1  # Initialize maxlength to 1 since the minimum sequence length is 1

        for i in range(0, len(nums)-1):
            if nums[i+1] == nums[i] + 1:
                length += 1
            else:
                maxlength = max(maxlength, length)
                length = 1
        
        # Final check to update maxlength in case the longest sequence is at the end
        maxlength = max(maxlength, length)
        
        return maxlength
