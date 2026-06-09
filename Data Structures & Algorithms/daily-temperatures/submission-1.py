class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        # create a stack which will hold (value, index)
        stack = []

        for i, value in enumerate(temperatures):
            # Evaluate stack to find the last value which is smaller than curr
            while stack and stack[-1][0] < value:
                stackValue, stackIndex = stack.pop()
                res[stackIndex] = i - stackIndex
            stack.append([value, i])
        
        return res

        
        