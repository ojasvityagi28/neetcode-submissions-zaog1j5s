class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        for i ,a in enumerate(nums):
            if target - a in hashset:
                return [hashset[target - a] ,i]
            hashset[a] = i
        