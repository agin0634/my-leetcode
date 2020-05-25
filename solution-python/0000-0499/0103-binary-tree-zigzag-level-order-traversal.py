# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return root
        queue, res = [root], []
        level = 0
        while len(queue):
            n = len(queue)
            tmp = []
            for i in range(n):
                q = queue.pop(0)
                tmp.append(q.val)
                if q.left:
                    queue.append(q.left)
                if q.right:
                    queue.append(q.right)
            if level % 2 == 0:
                res.append(tmp)
            else:
                res.append(tmp[::-1])
            level += 1
        return res