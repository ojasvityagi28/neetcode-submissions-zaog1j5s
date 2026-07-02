class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1 ,n):
                matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]

        def reverse(row):
            r = len(row) -1
            l = 0
            while l < r:
                row[l] , row[r] = row[r] , row[l]
                l +=1 
                r -= 1
        for row in matrix:
            reverse(row)
        
