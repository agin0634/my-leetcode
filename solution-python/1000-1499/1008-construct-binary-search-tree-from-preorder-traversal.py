# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        root = TreeNode(preorder[0])
        stack = [root]
        for i in range(1, len(preorder)):
            if preorder[i] < stack[-1].val:
                tmp = TreeNode(preorder[i])
                stack[-1].left = tmp
                stack.append(tmp)
            else:
                while stack and stack[-1].val < preorder[i]:
                    pop = stack.pop()
                tmp = TreeNode(preorder[i])
                pop.right = tmp
                stack.append(tmp)
        return root