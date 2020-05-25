# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.vals = set()
        def recover(node, x):
            if node:
                node.val = x
                self.vals.add(x)
                if node.left:
                    node.left = recover(node.left, 2*x+1)
                if node.right:
                    node.right = recover(node.right, 2*x+2)
                return node
            else:
                return None
        recover(root, 0)

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        return (target in self.vals)


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)