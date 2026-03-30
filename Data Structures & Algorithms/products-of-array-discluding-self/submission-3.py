class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        SProduct = 1
        PProduct = 1
        res = [1]*len(nums)
        i=1 #first number has no prefix
        while i < len(nums): #calculating prefix
            res[i] = nums[i-1]*PProduct
            PProduct *= nums[i-1]
            i+=1

        i= len(nums)-2 # last number has no suffix
        while i>=0:
            res[i] *= nums[i+1]*SProduct #multiplying w already present res[i]
            SProduct *= nums[i+1]
            i-=1
        return res



        

        