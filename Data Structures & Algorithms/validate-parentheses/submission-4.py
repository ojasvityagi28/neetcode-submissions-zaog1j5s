class Solution:
    def isValid(self, s: str) -> bool:
        matching = {"]":"[" , "}":"{" , ")" : "(" }

        stack = []

        for i in range(len(s)):
            if s[i] in matching:
                if not stack or stack[-1] != matching[s[i]]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(s[i])
        return not stack



        