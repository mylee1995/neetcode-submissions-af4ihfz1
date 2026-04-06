"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        return self.dfs(node, {})
        
    def dfs(self, node, visited):
        if node in visited:
            return visited[node]
        
        copy = Node(node.val)
        visited[node] = copy
        for nei in node.neighbors:
            copy.neighbors.append(self.dfs(nei, visited))

        return copy