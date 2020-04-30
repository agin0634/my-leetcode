# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def helper(node):
            if node:
                if node.left:
                    node.left = helper(node.left)
                if node.right:
                    node.right = helper(node.right)
                if node.val == 0 and not node.left and not node.right:
                    node = None
                return node
            else:
                return None
        return helper(root)