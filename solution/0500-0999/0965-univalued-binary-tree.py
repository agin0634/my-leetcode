# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.findValue(root, root.val)
        
    def findValue(self, node, val):
        if not node: 
            return True
        else:
            if node.val != val:
                return False
        return self.findValue(node.left, val) and self.findValue(node.right, val)