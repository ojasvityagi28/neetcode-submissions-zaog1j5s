from collections import deque
from math import isqrt
class Solution:
    def numSquares(self, n: int) -> int:
        queue = deque([n])
        visited = {n}
        steps = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                current = queue.popleft()

                if current == 0:
                    return steps
                for i in range(1, isqrt(current) + 1):
                    square = i * i
                    next_num = current - square
                    if next_num not in visited:
                        visited.add(next_num)
                        queue.append(next_num)
            steps += 1

        return -1