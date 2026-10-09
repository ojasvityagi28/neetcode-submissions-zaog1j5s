class Solution:
    def decodeString(self, s: str) -> str:
        number_stack = []
        string_stack = []
        num = 0
        current = ""
        i = 0

        while i < len(s):

            if s[i].isdigit():
                num = 0

                while i < len(s) and s[i].isdigit():
                    num = num*10 + int(s[i])
                    i += 1
                
            elif s[i] == "[":
                number_stack.append(num)
                string_stack.append(current)

                num = 0
                current = ""
                i += 1
            
            elif s[i] == "]":
                previous = string_stack.pop()
                number = number_stack.pop()

                current = previous + current*number
                i += 1
            else:
                current += s[i]
                i += 1
        
        return current


        
        