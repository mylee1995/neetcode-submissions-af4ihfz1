from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Check if start or end points are blocked
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
            
        n = len(grid)
        queue = deque([[0, 0]])  # Store as list for consistent unpacking
        visited = {(0, 0)}  # Keep set of tuples for visited
        dirs = [[1,0], [-1,0], [0,1], [0,-1], [1,1], [1,-1], [-1,-1], [-1,1]]
        path_length = 1
        
        while queue:
            # Process all nodes at current level
            for _ in range(len(queue)):
                [curr_x, curr_y] = queue.popleft()  # Unpack list coordinates
                
                # If we reached the target
                if curr_x == n-1 and curr_y == n-1:
                    return path_length
                    
                # Check all 8 directions
                for [dx, dy] in dirs:  # Unpack list directions
                    new_x = curr_x + dx
                    new_y = curr_y + dy
                    
                    # Check bounds, visited status, and if cell is clear
                    if (0 <= new_x < n and 
                        0 <= new_y < n and 
                        (new_x, new_y) not in visited and 
                        grid[new_x][new_y] == 0):
                        
                        queue.append([new_x, new_y])  # Append as list
                        visited.add((new_x, new_y))  # Add as tuple to set
            
            path_length += 1
            
        return -1
