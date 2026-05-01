class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        def dfs(i , j ):
            if j == len(word2):
                res = (len(word1) - i)
                dp[(i,j)] = res
                return res
            if (i , j) in dp:
                return dp[(i, j)]
            if i == len(word1):
                res = (len(word2) - j)
                dp[(i,j)] = res
                return res

            if ( j < len(word2)) and word1[i] != word2[j]:
                res = 1 + dfs(i + 1 , j) # skip it
                res = min(res , 1 + dfs(i + 1 , j + 1)) # replace it
                res = min(res , 1 + dfs( i , j + 1)) # insert it
            else:
                res = dfs(i + 1 , j + 1)
            dp[(i , j)] = res
            return dp[(i , j)]

        return dfs(0 , 0) 
        