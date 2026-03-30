class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for n in range(len(nums)):
            rem=target-nums[n]
            if rem in hashmap:
                return hashmap[rem],n
            hashmap[nums[n]]=n
        


        