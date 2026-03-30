class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        position ={}
        l = 0
        max_substring = 0
        for r in range(len(s)):
            #check if theres a previous position and if its in bound of the window
            if s[r] in position and position[s[r]]  >= l:
                l =position[s[r]]+1 #the new window starts from the previous duplicate char position +=1
            max_substring = max(max_substring, r-l+1)
            #update the dict to the new position of r
            position[s[r]]  = r
        return max_substring

        