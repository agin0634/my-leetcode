# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.stack = []
        self.in_Order(root)
        self.res = TreeNode(self.stack.pop())
        while self.stack:
            t = TreeNode(self.stack.pop())
            t.left = None
            t.right = self.res
            self.res = t
        return self.res
        
    def in_Order(self, node):
        if node:
            self.in_Order(node.left) 
            self.stack.append(node.val)
            self.in_Order(node.right) 
        return None