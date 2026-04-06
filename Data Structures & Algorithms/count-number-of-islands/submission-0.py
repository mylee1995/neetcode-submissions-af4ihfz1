class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        hashMap = {}
        row = len(grid)
        col = len(grid[0])
        numIslands = 0

        for i in range(0, row):
            for j in range (0, col):
                key = "{}{}".format(i, j)
                if grid[i][j] == "1" and key not in hashMap:
                    self.dfs(grid, hashMap, i , j)
                    numIslands += 1
        
        return numIslands
    
    def dfs(self, grid: List[List[str]], visitedMap, i,j):
        if i < 0 or j < 0:
            return
        if i >= len(grid) or j >= len(grid[0]):
            return
        
        key = "{}{}".format(i, j)
        if key in visitedMap:
            return

        if grid[i][j] == "1":
            visitedMap[key] = True
            self.dfs(grid, visitedMap, i-1, j)
            self.dfs(grid, visitedMap, i+1, j)
            self.dfs(grid, visitedMap, i, j-1)
            self.dfs(grid, visitedMap, i, j+1)
        else:
            return
        
        
