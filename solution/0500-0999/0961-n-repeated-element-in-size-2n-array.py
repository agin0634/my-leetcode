class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A)/2
        for a in A:
            if A.count(a) == N:
                return a