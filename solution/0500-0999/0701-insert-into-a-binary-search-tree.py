# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            root = TreeNode(val)
            return root
        
        def helper(node, val):
            if val > node.val:
                if not node.right:
                    node.right = TreeNode(val)
                else:
                    helper(node.right, val)
            else:
                if not node.left:
                    node.left = TreeNode(val)
                else:
                    helper(node.left, val)
        helper(root, val)
        return root