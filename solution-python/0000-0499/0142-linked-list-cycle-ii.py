# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dict = {}
        pos = 0
        while head:
            if head in dict:
                return head
            else:
                dict[head] = pos
                pos += 1
            head = head.next
        return None