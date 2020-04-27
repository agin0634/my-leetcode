# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue, res= [root], 0
        while len(queue) > 0:
            res = queue[0].val
            n = len(queue)
            for i in range(n):
                q = queue.pop(0)
                if q.left:
                    queue.append(q.left)
                if q.right:
                    queue.append(q.right)
        return res