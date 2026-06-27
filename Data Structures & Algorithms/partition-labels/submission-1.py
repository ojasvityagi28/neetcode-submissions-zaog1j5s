class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}

        for i in range(len(s) - 1 , -1 , -1):
            if s[i] not in last_index:
                last_index[s[i]] = i
        start = 0
        end = 0
        res = []

        for i,c in enumerate(s):
            end = max(last_index[c] , end)

            if i == end:
                res.append(end - start + 1)
                start = i + 1
        return res
                    