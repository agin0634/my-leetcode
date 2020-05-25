# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        sums = []
        def helper(node, sum):
            if not node: return 
            if not node.left and not node.right:
                sums.append(sum + node.val)
                return
            helper(node.left, sum + node.val)
            helper(node.right, sum + node.val)
        helper(root, 0)
        return sum in sums