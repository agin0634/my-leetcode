# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.hashmap = {}
        self.dfs(root, 0)
        return self.hashmap[max(self.hashmap)]
        
    def dfs(self, node, depth):
        if node:
            depth += 1
            if node.left:
                self.dfs(node.left, depth)
            if node.right:
                self.dfs(node.right, depth)
        if depth not in self.hashmap:
            self.hashmap[depth] = node.val
        else:
            self.hashmap[depth] += node.val