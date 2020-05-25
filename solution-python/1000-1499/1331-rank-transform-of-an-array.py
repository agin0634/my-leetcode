class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        dict = {}
        A = sorted(set(arr))
        for i,e in enumerate(A):
            dict[e] = i+1
        return [dict[a] for a in arr]