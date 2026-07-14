class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft = [0]*n
        maxRight = [0]*n
        l = 0
        r = 0
        res = 0
        for i in range(n):
            maxLeft[i] = l
            l = max(l , height[i])
        for i in range(n - 1, -1 , -1):
            maxRight[i] = r
            r = max(r , height[i])
        for i in range(n):
            total = min(maxLeft[i], maxRight[i]) - height[i]
            if total < 0:
                total = 0
            res += total
        return res
        

        