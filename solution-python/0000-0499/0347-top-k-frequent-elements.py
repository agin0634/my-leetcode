class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict = {}
        for n in nums:
            dict[n] = dict.get(n, 0) + 1
        return heapq.nlargest(k, dict, key=dict.get)