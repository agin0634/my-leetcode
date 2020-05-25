class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for n in range(numRows):
            row = [1]*(n+1)
            for i in range(1,n):
                row[i] = res[n-1][i-1] + res[n-1][i]
            res.append(row)
        return res