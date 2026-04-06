# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.maxDepthDFS(root, 0)
    
    def maxDepthDFS(self, node: Optional[TreeNode], depth: int) -> int:
        if node == None:
            return depth
        
        left = self.maxDepthDFS(node.left, depth+1)
        right = self.maxDepthDFS(node.right, depth+1)
        
        return max(left,right)
        