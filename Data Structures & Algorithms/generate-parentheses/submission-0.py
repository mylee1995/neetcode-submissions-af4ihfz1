class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.dfs("", n, n, result)
        return result
        
    def dfs(self, current: str, openParen: int, closeParen: int, result: List[str]):
        # Base case: when both open and close parentheses are used up
        if openParen == 0 and closeParen == 0:
            result.append(current)
            return
            
        # If we have remaining open parentheses, we can add an open parenthesis
        if openParen > 0:
            self.dfs(current + "(", openParen - 1, closeParen, result)
            
        # We can add a closing parenthesis if we have more close parentheses than open ones
        if closeParen > openParen:
            self.dfs(current + ")", openParen, closeParen - 1, result)
