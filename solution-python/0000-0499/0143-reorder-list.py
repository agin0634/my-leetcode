# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        
        stack = []
        while head.next.next:
            stack.append(head.next.val)
            head.next = head.next.next
        r = temp = ListNode(0)
        c = 0
        while stack:
            if c == 0:
                n = stack[0]
                del stack[0]
                temp.next = ListNode(n)
                temp = temp.next
                c = 1
            else:
                n = stack.pop()
                temp.next = ListNode(n)
                temp = temp.next
                c = 0
        head.next.next = r.next
            