import math
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = w = res = sum(weights)

        while l <= r:
            mid = (l + r)//2
            load = 0
            d = 1
            for wt in weights:
                if wt + load > mid:
                    d += 1
                    load = 0
                load += wt

            if d <= days:
                res = min(mid , res)
                r = mid - 1
            else:
                l = mid + 1
        return res