# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    res = ""
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t: return self.res
        self.res += str(t.val)
        if t.left:
            self.res += "("
            self.tree2str(t.left)
            self.res += ")"
        if t.right:
            if not t.left:
                self.res += "()"
            self.res += "("
            self.tree2str(t.right)
            self.res += ")"
        return self.res