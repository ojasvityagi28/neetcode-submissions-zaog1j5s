class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        countMap = {}

        for word in strs:
            ordered = tuple(sorted(word))
            if ordered not in countMap:
                countMap[ordered] = []
            countMap[ordered].append(word)
        return list(countMap.values())

        