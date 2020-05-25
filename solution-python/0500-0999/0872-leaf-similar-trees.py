# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        self.S1, self.S2 = [], []
        self.findLeaf(root1, self.S1)
        self.findLeaf(root2, self.S2)
        return self.S1 == self.S2
    
    def findLeaf(self, node, stack):
        if node:
            self.findLeaf(node.left, stack)
            self.findLeaf(node.right, stack)
            if not node.left and not node.right:
                stack.append(node.val)
        return None