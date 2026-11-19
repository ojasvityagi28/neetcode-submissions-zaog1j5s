class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        MOD = 10**9 + 7

        stack = []  # (minimum, count)
        cur_sum = 0
        res = 0

        for num in arr:
            count = 1

            while stack and stack[-1][0] >= num:
                val, cnt = stack.pop()
                cur_sum -= val * cnt
                count += cnt

            stack.append((num, count))
            cur_sum += num * count

            res += cur_sum

        return res % MOD