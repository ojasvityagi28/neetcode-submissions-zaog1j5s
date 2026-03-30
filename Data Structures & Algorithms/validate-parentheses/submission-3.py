class Solution:
    def isValid(self, s: str) -> bool:
        hashmap={")":"(", "}":"{", "]" :"[" }
        stack=[]
        for char in s:
            if char not in hashmap:
                stack.append(char)
            else:
                if not stack or stack[-1]!= hashmap[char]:
                    return False
                stack.pop()

        return not stack


        