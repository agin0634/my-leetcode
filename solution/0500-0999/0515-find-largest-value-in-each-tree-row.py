# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return root
        queue, res = [root], []
        while len(queue) > 0:
            n = len(queue)
            max = float('-inf')
            for i in range(n):
                q = queue.pop(0)
                if q.val > max:
                    max = q.val
                if q.left:
                    queue.append(q.left)
                if q.right:
                    queue.append(q.right)
            res.append(max)
        return res