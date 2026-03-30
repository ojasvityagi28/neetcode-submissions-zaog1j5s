class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in "+-/*":
                a = stack.pop()
                b = stack.pop()
                if tokens[i] == "+":
                    val = b+a
                elif tokens[i] == "-":
                    val = b-a
                elif tokens[i] == "*":
                    val = b*a
                elif tokens[i] == "/":
                    val = int(b/a)
                stack.append(val)
            else:
                stack.append(int(tokens[i]))
    
        return stack[-1]
                
            

        