# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        res = [None]*k
        temp = root
        length, size = 0, []
        while temp:
            length += 1
            temp = temp.next
            
        size = [length//k]*k
        r = length%k
        for i in range(r):
            size[i] += 1
            
        for j in range(len(size)):
            r = curr = ListNode(0)
            for s in range(size[j]):
                curr.next = ListNode(root.val)
                root = root.next
                curr = curr.next
            res[j] = r.next
        return res