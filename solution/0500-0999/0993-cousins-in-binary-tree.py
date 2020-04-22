# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        queue = [(-1, root)]
        while len(queue) > 0:
            i = len(queue)
            hashmap = dict()
            for _ in range(i):
                parent, node = queue.pop(0)
                hashmap[node.val] = parent
                if node.left:
                    queue.append((node.val, node.left))
                if node.right:
                    queue.append((node.val, node.right))
                if x in hashmap and y in hashmap:
                    if hashmap[x] == hashmap[y]:
                        return False 
                    else:
                        return True
        return False