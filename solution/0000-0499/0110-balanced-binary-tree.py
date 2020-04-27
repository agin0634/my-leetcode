# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.res = True
        self.dfs(root, 0)
        return self.res
        
    def dfs(self, node, depth):
        if not node: return 0
        L = self.dfs(node.left, depth)
        R = self.dfs(node.right, depth)
        d = max(L, R)
        if abs(L - R) > 1:
            self.res = False
        return d+1