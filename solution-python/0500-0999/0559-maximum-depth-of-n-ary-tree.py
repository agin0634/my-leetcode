"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        self.depth = 0
        self.findDepth(root, 0)
        return self.depth
    
    def findDepth(self, node, depth):
        if node:
            depth += 1
            for c in node.children:
                self.findDepth(c, depth)
        if depth > self.depth:
            self.depth = depth
        return None