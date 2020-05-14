class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        max_in_col, min_in_row = [], []
        res = []
        for i in range(len(matrix[0])):
            max = float('-inf')
            for j in range(len(matrix)):
                if matrix[j][i] > max:
                    max = matrix[j][i]
            max_in_col.append(max)
        for m in matrix:
            n = min(m)
            if n in max_in_col:
                res.append(n)
        return res