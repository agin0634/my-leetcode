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
        if not root:
            return None
        
        self.res = []
        self.dfs(root)
        self.res.append(root.val)
        return self.res
                
    def dfs(self, node):
        if not node.children:
            return 
        else:
            for c in node.children:
                self.dfs(c)
                self.res.append(c.val)