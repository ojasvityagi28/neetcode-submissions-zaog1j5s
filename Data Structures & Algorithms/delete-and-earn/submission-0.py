class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        total = {n : 0 for n in nums}

        for n in nums:
            total[n] += n
        nums = []
        for n in total:
            nums.append(n)
        nums.sort()

        prev1, prev2 = 0 , 0

        for i in range(len(nums)):
            if i > 0 and nums[i] != nums[i - 1] + 1:
                curr = prev1 + total[nums[i]]
                prev2 = prev1
                prev1 = curr
            else:
                curr = max(prev2 + total[nums[i]], prev1)
                prev2 = prev1
                prev1 = curr
        return prev1
