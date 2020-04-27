# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return root
        queue, max, level, res= [root], float("-inf"), 0, 0
        while len(queue):
            n = len(queue)
            tmp = 0
            level += 1
            for _ in range(n):
                q = queue.pop(0)
                tmp += q.val
                if q.left:
                    queue.append(q.left)
                if q.right:
                    queue.append(q.right)
            if tmp > max:
                max = tmp
                res = level
        return res