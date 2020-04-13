# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        res = r = ListNode(0)
        while lists:
            curr = float('inf')
            count = 0
            for i,e in enumerate(lists):
                if e and e.val < curr:
                    curr = e.val
                    count = i
            if lists[count] == None:
                break
            r.next = ListNode(lists[count].val)
            r = r.next
            lists[count] = lists[count].next
        return res.next