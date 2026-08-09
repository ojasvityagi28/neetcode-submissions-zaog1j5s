class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        def dfs(i , j):
            if i == len(word1) and j == len(word2):
                return 0
            if j == len(word2):
                return len(word1) - i

            if i == len(word1):
                return len(word2) - j

            if (i, j) in dp:
                return dp[(i,j)]

            if word1[i] != word2[j]:
                a = dfs(i , j + 1)
                b = dfs(i + 1, j)
                c = dfs(i + 1, j + 1)

                dp[(i , j)] = min(1 + a, 1 + b, 1 + c) 
            else:
                dp[(i , j)] = dfs(i + 1, j + 1)

            return dp[(i , j)]
        return dfs(0 , 0)