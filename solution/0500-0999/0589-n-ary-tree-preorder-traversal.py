"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        self.res = []
        self.dfs(root)
        return self.res
        
    def dfs(self, n):
        if n:
            self.res.append(n.val)
            for i in n.children:
                self.dfs(i)