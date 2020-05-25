# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root: return root
        queue, res= [root], []
        while len(queue) > 0:
            n = len(queue)
            sum = 0
            for i in range(n):
                q = queue.pop(0)
                sum += q.val
                if q.left:
                    queue.append(q.left)
                if q.right:
                    queue.append(q.right)
            res.append(float(sum)/n)
        return res