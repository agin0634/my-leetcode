# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.hashmap = dict()
        return self.dfs(root, k)
        
    def dfs(self, node, target):
        if not node: return False
        d = target - node.val
        print d
        if node.val in self.hashmap:
            res = True
        else:
            self.hashmap[d] = True
            res = False
        return res or self.dfs(node.left, target) or self.dfs(node.right, target)