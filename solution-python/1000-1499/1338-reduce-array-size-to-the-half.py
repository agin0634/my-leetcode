class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        dict, h , count, res= {}, len(arr)/2, 0, 0
        for i in arr:
            dict[i] = dict.get(i, 0)+1
        V = sorted(dict.values())
        while count < h:
            count += V.pop()
            res += 1
        return res