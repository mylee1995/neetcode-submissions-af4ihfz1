class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # [index, val]

        for i, val in enumerate(temperatures):
            while stack and stack[-1][1] < val:
                popped_index, popped_val = stack.pop()
                result[popped_index] = i - popped_index
            stack.append([i, val])
        return result