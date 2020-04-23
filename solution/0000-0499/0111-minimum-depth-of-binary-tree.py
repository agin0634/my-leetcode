# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        queue, depth = [root], 0
        isLeaf = False
        while len(queue) > 0 and isLeaf == False:
            depth += 1
            n = len(queue)
            for i in range(n):
                q = queue.pop(0)
                if not q.left and not q.right:
                    isLeaf = True
                    break
                if q.left:
                    queue.append(q.left)
                if q.right:
                    queue.append(q.right)
        return depth