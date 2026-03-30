class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output = [1] * length
        for i in range(len(nums)):
            output[i]=1
            for j in range(len(nums)):
                if j!=i:
                    output[i] *= nums[j]
        return output

        