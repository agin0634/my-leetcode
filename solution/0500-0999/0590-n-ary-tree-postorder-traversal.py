"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        self.res = []
        self.dfs(root)
        return self.res
        
    def dfs(self, node):
        if node:
            for c in node.children:
                self.dfs(c)
            self.res.append(node.val)
        return None