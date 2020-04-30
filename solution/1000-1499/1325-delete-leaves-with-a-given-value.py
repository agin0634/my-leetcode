# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        self.t = target
        return self.dfs(root)
        
    def dfs(self, node):
        if node:
            if node.left:
                node.left = self.dfs(node.left)
            if node.right:
                node.right = self.dfs(node.right)
            if node.val == self.t and not node.left and not node.right:
                node = None
        return node