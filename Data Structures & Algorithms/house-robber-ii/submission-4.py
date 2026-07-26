class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
    
        a = self.rob1(nums[0 : len(nums) - 1])
        b = self.rob1(nums[1 : len(nums)])
        return max(a , b)

    def rob1(self , nums: List[int]) -> int:
        prev1 , prev2 = 0 , 0

        for n in nums:
            tmp = prev1
            prev1 = max(prev2 + n , prev1)
            prev2 = tmp
        return prev1


        
        