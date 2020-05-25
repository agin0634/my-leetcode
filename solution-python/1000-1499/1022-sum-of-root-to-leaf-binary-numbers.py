# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.dfs(root, "")
        return self.res
        
    def dfs(self, node, val):
        if node:
            val += str(node.val)
            self.dfs(node.left, val)
            self.dfs(node.right, val)
            if not node.left and not node.right:
                self.res += int(val, 2)
        return None