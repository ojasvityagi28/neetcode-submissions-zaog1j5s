class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        hashmaps1={}
        for a in s1:
            hashmaps1[a] = 1+ hashmaps1.get(a,0)
        l = 0
        for r in range(len(s2)):
            while (s2[r] not in hashmaps1) or (hashmaps1[s2[r]]==0):
                if l < r:
                    if s2[l] in hashmaps1:
                        hashmaps1[s2[l]] +=1
                    l += 1
                else:
                    l = r + 1
                    break
            
            if s2[r] in hashmaps1 and hashmaps1[s2[r]] > 0:
                hashmaps1[s2[r]] -= 1
                if (r-l+1) == len(s1):
                   return True

        return False