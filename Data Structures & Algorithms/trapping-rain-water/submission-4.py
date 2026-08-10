class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = height[0]
        maxRight = height[-1]
        l = 0
        r = len(height) - 1
        res = 0
        while l < r:
            if maxLeft <= maxRight:
                l += 1
                total = maxLeft - height[l]
                res += total if total > 0 else 0
                maxLeft = max(maxLeft , height[l])
            else:
                r -= 1
                total = maxRight - height[r]
                res += total if total > 0 else 0
                maxRight = max(maxRight , height[r])
        return res






        