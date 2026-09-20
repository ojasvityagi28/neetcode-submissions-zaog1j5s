class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        countmap = {}

        for s in strs:
            arrcount = [0]*26
            for char in s:
                index = ord(char) - ord('a')
                arrcount[index] +=1
            if tuple(arrcount) not in countmap:
                countmap[tuple(arrcount)] = []
            countmap[tuple(arrcount)].append(s)
        return list(countmap.values())

        