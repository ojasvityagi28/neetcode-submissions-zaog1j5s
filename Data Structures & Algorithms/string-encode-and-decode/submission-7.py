class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for w in strs:
            length = 0
            for c in w:
                length+=1
            res += str(length) + "#" + w
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j]!= "#":
                j+= 1
            length = int(s[i : j])
            word = s[j + 1 : j + 1 + length]
            res.append(word)
            i = j + 1 + length 
        return res
        


        
        
