from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        for row in range(0, ROWS):
            for col in range(0, COLS):
                if grid[row][col] == 0:
                    queue.append([row, col])
                    visited.add((row, col))

        def addCell(r, c):
            if (0 <= r < ROWS and 0 <= c < COLS and (r,c) not in visited and grid[r][c] != -1):
                visited.add((r, c))
                queue.append([r, c])

        
        dist = 0
        while queue:
            for _ in range(len(queue)):
                [r, c] = queue.popleft()
                grid[r][c] = dist
                addCell(r+1, c)
                addCell(r, c+1)
                addCell(r, c-1)
                addCell(r-1, c)
            dist += 1

        