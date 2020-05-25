"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root: return root
        queue, res = [root], [[root.val]]
        while len(queue) > 0:
            n = len(queue)
            tmp = []
            for i in range(n):
                q = queue.pop(0)
                for c in q.children:
                    tmp.append(c.val)
                    queue.append(c)
            if tmp:
                res.append(tmp)
        return res