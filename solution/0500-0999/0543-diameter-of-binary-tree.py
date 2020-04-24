# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diameter = 0
        self.helper(root)
        return self.diameter
    
    def helper(self, node):
        if not node: return 0
        L = self.helper(node.left)
        R = self.helper(node.right)
        path = L + R
        if path > self.diameter:
            self.diameter = path
        return max(L, R) + 1