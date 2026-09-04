class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(i , n):
                if i != j:
                    matrix[i][j] ,matrix[j][i] = matrix[j][i] , matrix[i][j]
            l = 0
            r = m - 1
            while l < r:
                matrix[i][l] , matrix[i][r] = matrix[i][r] , matrix[i][l]
                l += 1
                r -= 1
        

        