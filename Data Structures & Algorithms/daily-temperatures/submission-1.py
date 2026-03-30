class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)

        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                a,b = stack.pop()
                result[b] = i-b #new higher temp index - prev temp index
            stack.append((temperatures[i],i))

        return result
            

        