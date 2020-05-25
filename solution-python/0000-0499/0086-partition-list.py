# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        gr = g = ListNode(0)
        lr = l = ListNode(0)
        while head:
            if head.val < x:
                l.next = ListNode(head.val)
                l = l.next
            else:
                g.next = ListNode(head.val)
                g = g.next
            head = head.next
        l.next = gr.next
        return lr.next