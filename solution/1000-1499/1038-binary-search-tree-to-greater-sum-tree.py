# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    sum = 0
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return root
        if root.right:
            self.bstToGst(root.right)
        self.sum += root.val
        root.val = self.sum
        if root.left:
            self.bstToGst(root.left) 
        return root