class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        change = [0]*1001

        for passengers, start, end in trips:
            change[start] += passengers
            change[end] -= passengers
        
        current = 0

        for i in range(1001):
            current += change[i]
            if current > capacity:
                return False
        return True