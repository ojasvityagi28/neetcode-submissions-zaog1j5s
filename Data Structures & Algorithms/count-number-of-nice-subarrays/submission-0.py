class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        odd_count = {0 : 1}
        res = 0
        odd = 0

        for r in range(len(nums)):
            if nums[r] % 2:
                odd += 1
            
            target = odd - k

            if target in odd_count:
                res += odd_count[target]

            if odd not in odd_count:
                odd_count[odd] = 0

            odd_count[odd] += 1
        return res
