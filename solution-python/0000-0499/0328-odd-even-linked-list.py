# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd_head = odd = ListNode(0)
        even_head = even = ListNode(0)
        count = 1
        while head:
            if count % 2 == 0: 
                even.next = head
                even = even.next
            else:              
                odd.next = head
                odd = odd.next
            count += 1
            head = head.next
        even.next = None
        odd.next = even_head.next
        return odd_head.next