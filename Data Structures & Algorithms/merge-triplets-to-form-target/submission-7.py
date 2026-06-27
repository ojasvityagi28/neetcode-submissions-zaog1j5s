class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        needed = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i , n in enumerate(t):
                if n == target[i]:
                    needed.add(i)
        return len(needed) == 3

        