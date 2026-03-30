class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dict1,dict2={},{}
        for l in range(len(s)):
            dict1[s[l]]=1+dict1.get(s[l],0)
            dict2[t[l]]=1+dict2.get(t[l],0)
        for a in dict1:
            if dict1[a]!=dict2.get(a,0):
                return False
        return True

        