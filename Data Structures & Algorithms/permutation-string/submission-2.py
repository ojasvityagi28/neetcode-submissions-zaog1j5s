class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap={}
    
        for s in s1:
            hashmap[s]=1+hashmap.get(s,0)

        for l in range(len(s2)):
            r=l
            temp_map = hashmap.copy()
            
            while r < len(s2) and s2[r] in temp_map and temp_map[s2[r]]!=0:
                temp_map[s2[r]]-=1
                r+=1

            if (r-l)==len(s1):
                return True
            
        return False


        