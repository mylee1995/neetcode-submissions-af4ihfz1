class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # ((1 + 2) * 3) - 4 = 5
        # ((1 + 2) * 3) = 5 + 4
        # ((1 + 2) = (5 + 4) / 3
        stack = []
        for token in tokens:
            if token == "+":
                a, b = stack.pop(), stack.pop()
                stack.append(a+b)
            elif token == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif token == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b/a)))
            elif token == "*":
                a, b = stack.pop(), stack.pop()
                stack.append(a*b)
            else:
                stack.append(int(token))
        return stack[0]