class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0 : 1}
        running = 0
        res = 0

        for r in range(len(nums)):
            running += nums[r]

            if (running - k) in prefix:
                res += prefix[running - k]
            
            prefix[running] = 1 + prefix.get(running, 0)

        return res


        