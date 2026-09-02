class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = height[0]
        maxRight = height[-1]
        l = 1
        r = len(height) - 2
        res = 0
        while l <= r:
            if maxLeft <= maxRight:
                total = maxLeft - height[l]
                res += total if total > 0 else 0
                maxLeft = max(maxLeft , height[l])
                l += 1 #next to be processed
            else:
                total = maxRight - height[r]
                res += total if total > 0 else 0
                maxRight = max(maxRight , height[r])
                r -= 1
        return res






        