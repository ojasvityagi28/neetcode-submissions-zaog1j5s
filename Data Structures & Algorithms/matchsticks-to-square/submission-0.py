class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False
        side = sum(matchsticks)//4
        sides = [0]*4
        matchsticks.sort(reverse=True)

        def dfs(i):
            if i == len(matchsticks):
                return True  # every stick placed
            tried_sums = set()

            for s in range(4):
                if sides[s] + matchsticks[i] > side:
                    continue
                if sides[s] in tried_sums:
                    continue
                tried_sums.add(sides[s])
                sides[s] += matchsticks[i]
                if dfs(i + 1):
                    return True
                sides[s] -= matchsticks[i]
            return False
        return dfs(0)
                






            
