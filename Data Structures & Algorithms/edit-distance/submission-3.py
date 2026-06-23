class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        def dfs(i , j):
            if j == len(word2):
                return len(word1) - i #to delete them
            if i == len(word1):
                return len(word2) - j #to insert them
            if (i , j) in dp:
                return dp[(i , j)]

            if word1[i] != word2[j]:
                res = min(1 + dfs(i + 1 , j),1 + dfs(i , j + 1)) # insert it
                res  = min(res ,1 + dfs(i + 1 , j + 1)) #replace it
            else:
                res = dfs(i + 1 , j + 1)
            dp[(i ,j)] = res
            return dp[(i , j)]

        return dfs(0 , 0)


                


        