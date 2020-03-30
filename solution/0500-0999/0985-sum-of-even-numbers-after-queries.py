class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        S = sum(a for a in A if a % 2 == 0)
        res = []
        
        for q in queries:
            v,i = q
            if A[i] % 2 == 0:
                S -= A[i]
            A[i] += v
            if A[i] % 2 == 0:
                S += A[i]
            res.append(S)
        return res