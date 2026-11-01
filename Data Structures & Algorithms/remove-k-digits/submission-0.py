class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        n = len(num)

        for i in range(len(num)):
            while stack and int(stack[-1]) > int(num[i]) and k > 0:
                k -= 1
                stack.pop()
            stack.append(num[i])
        
        res = ''.join(stack[:len(stack) - k]).lstrip("0")
        
        return res if res else "0"

        