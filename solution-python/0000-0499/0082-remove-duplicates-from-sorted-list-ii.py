# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = curr = ListNode(0)
        if not head or not head.next:
            return head
        
        while head and head.next:
            if head.val == head.next.val:
                c = head.val
                while head and head.val == c:
                    head = head.next
                curr.next = head
            else:
                curr.next = head
                curr = curr.next
                head = head.next
            
        return res.next