import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 0:
            return 0
        result = []
        for i in range (0, len(tokens)):
            if tokens[i] == "+":
                right, left = result.pop(), result.pop()
                result.append(left + right)
            elif tokens[i] == "-":
                right, left = result.pop(), result.pop()
                result.append(left - right)
            elif tokens[i] == "*":
                right, left = result.pop(), result.pop()
                result.append(left * right)
            elif tokens[i] == "/":
                right, left = result.pop(), result.pop()
                result.append(int((left) / right))
            else:
                result.append(int(tokens[i]))
        
        return result[0]