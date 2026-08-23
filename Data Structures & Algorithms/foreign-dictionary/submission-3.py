class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjlist = {c : set() for word in words for c in word}

        for i in range(len(words) - 1):
            w1 , w2 = words[i] , words[i + 1]
            minLen = min(len(w1) , len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adjlist[w1[j]].add(w2[j])
                    break
        res = []
        visited = {} #0 for visiting, 1 for visited
        def dfs(c):
            if c in visited:
                return visited[c] == 0
            visited[c] = 0

            for nei in adjlist[c]:
                if dfs(nei):
                    return True

            visited[c] = 1
            res.append(c)

            return False

        for c in adjlist:
            if c not in visited:
                if dfs(c):
                    return ""

        res.reverse()
        return "".join(res)




        