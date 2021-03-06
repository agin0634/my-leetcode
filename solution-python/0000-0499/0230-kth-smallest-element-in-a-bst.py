# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.tmp = []
        self.helper(root)
        return self.tmp[k-1]
        
    def helper(self, node):
        if node:
            self.helper(node.left)
            self.tmp.append(node.val)
            self.helper(node.right)
        return