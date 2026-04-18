class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjlist = {c : set() for w in words for c in w}

        for i in range(len(words)-1):
            w1 , w2 = words[i], words[i+1]
            minlength = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minlength] == w2[:minlength]:
                return ""
            for j in range(minlength):
                if w1[j] != w2[j]:
                    adjlist[w1[j]].add(w2[j])
                    break
        res = []
        visit= {c : 0 for c in adjlist}
        def dfs(c):
            if visit[c] == 1:
                return True
            if visit[c] == 2:
                return False
            visit[c] = 1
            for nei in adjlist[c]:
                if dfs(nei):
                    return True
            visit[c] = 2
            res.append(c)
            return False

        for c in adjlist:
            if dfs(c):
                return ""
        return "".join(res[::-1])
