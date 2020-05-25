# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.depth = 0
        self.dfs(root, self.depth)
        return self.depth
        
    def dfs(self, node, depth):
        if node:
            depth += 1
            self.dfs(node.left, depth)
            self.dfs(node.right, depth)
        if depth > self.depth:
            self.depth = depth
        return None  