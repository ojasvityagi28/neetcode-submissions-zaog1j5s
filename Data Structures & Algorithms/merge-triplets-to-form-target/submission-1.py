class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        rows = len(triplets)
        cols = len(triplets[0])
        maximum = [0]*cols
        for i in range(rows):
            flag = True
            for j in range(cols):
                if triplets[i][j] > target[j]:
                    flag = False
            if not flag:
                continue
            for j in range(cols):
                maximum[j] = max(triplets[i][j] , maximum[j])
                    
        return maximum == target
                
                
        