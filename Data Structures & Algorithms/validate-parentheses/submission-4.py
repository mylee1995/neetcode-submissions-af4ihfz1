class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True

        stack = []
        for i in range(0, len(s)):
            c = s[i]
            if c == "[":
                stack.append("]")
            elif c == "]":
                if len(stack) == 0 or stack.pop() != c:
                    return False
            elif c == "{":
                stack.append("}")
            elif c == "}":
                if len(stack) == 0 or stack.pop() != c:
                    return False
            elif c == "(":
                stack.append(")")
            elif c == ")":
                if len(stack) == 0 or stack.pop() != c:
                    return False
            else:
                raise NotImplementedError

        return len(stack) == 0