class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        q = deque()
        q.append(0)
        steps = 0
        visited = set()
        while q:
            steps += 1
            length = len(q)
            for i in range(length):
                index = q.popleft()
                for j in range(1 , nums[index] + 1):
                    if (index + j) not in visited:
                        visited.add(index + j)
                        q.append(index + j)
                    if index + j == len(nums) - 1:
                        return steps
        
            
        