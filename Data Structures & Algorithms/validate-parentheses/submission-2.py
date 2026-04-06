class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching_map = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        for c in s:
            if c in matching_map:
                if len(stack) == 0:
                    return False
                last_elem = stack[len(stack) -1]
                if last_elem == matching_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if len(stack) > 0:
            return False
        return True