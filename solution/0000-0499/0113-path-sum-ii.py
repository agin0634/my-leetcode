# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        def helper(node, tmp):
            if not node: return 
            if not node.left and not node.right:
                tmp += [node.val]
                if sum(tmp) == s:
                    res.append(tmp)
                return
            helper(node.left, tmp + [node.val])
            helper(node.right, tmp + [node.val])
        helper(root, [])
        return res