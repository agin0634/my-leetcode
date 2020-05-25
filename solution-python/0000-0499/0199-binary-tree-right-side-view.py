# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return root
        queue, res = [root], []
        while len(queue):
            n = len(queue)
            res.append(queue[-1].val)
            for _ in range(n):
                q = queue.pop(0)
                if q.left:
                    queue.append(q.left)
                if q.right:
                    queue.append(q.right)
        return res