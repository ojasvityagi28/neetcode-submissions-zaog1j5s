class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        indexmap = {}

        for i , c in enumerate(s):
            indexmap[c] = i
        res = []
        start = 0
        end = 0
        for i , c in enumerate(s):
            end = max(indexmap[c] , end)

            if i == end:
                res.append(end - start + 1)
                start = i + 1
        return res

        