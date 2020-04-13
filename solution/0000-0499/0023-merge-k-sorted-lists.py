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
        heap = []
        for i in lists:
            while i:
                heap.append(i.val)
                i = i.next
        heap = sorted(heap)
        
        for h in heap:
            r.next = ListNode(h)
            r = r.next
        return res.next