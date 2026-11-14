class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        count = [[0 , 0] for i in range(len(strs))]

        for i ,s in enumerate(strs):
            for char in s:
                if char == "1":
                    count[i][1] += 1
                else:
                    count[i][0] += 1
        dp = {}

        def dfs(b, zero_count, one_count):
            if b == len(strs):
                return 0

            if (b, zero_count, one_count) in dp:
                return dp[(b, zero_count, one_count)]

            res = dfs(b + 1, zero_count, one_count)              # skip strs[b]

            if zero_count + count[b][0] <= m and one_count + count[b][1] <= n:
                res = max(res, 1 + dfs(b + 1, zero_count + count[b][0], one_count + count[b][1]))   # take strs[b]

            dp[(b, zero_count, one_count)] = res
            return res

        return dfs(0, 0, 0)