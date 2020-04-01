# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        G = set(G)
        res = 0
        curr = head
        while curr:
            if curr.val in G and getattr(curr.next, 'val', None)  not in G:
                res += 1
            curr = curr.next
        return res