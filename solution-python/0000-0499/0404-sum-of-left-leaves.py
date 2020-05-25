# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node):
            sum = 0
            if node:
                if node.left and not node.left.left and not node.left.right:
                    sum += node.left.val
                sum += helper(node.left)
                sum += helper(node.right)
                return sum
            else:
                return 0
        return helper(root)