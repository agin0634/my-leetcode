class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        if n % 2 == 0:
            for i in range(1,n/2+1):
                res.append(i*1)
                res.append(i*-1)
        else:
            res.append(0)
            for i in range(1,(n-1)/2+1):
                res.append(i*1)
                res.append(i*-1)
        return res