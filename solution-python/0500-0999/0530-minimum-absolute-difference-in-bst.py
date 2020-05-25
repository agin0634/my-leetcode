# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    val, min = float("-inf"), float("inf")
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return root
        self.getMinimumDifference(root.left)
        self.val, self.min = root.val, min(self.min, root.val-self.val)
        self.getMinimumDifference(root.right)
        return self.min