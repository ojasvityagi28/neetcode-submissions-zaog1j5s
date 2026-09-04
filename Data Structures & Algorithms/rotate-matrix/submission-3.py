class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(i + 1, m): 
                if i != j:
                    matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]
            l , r = 0 , len(matrix[i]) - 1
            while l < r:
                matrix[i][l] , matrix[i][r]  = matrix[i][r] , matrix[i][l]
                l += 1
                r -= 1
           