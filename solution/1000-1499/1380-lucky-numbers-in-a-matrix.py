class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        min_row = {min(i) for i in matrix}
        max_col = {max(j) for j in zip(*matrix)}
        return list(max_col & min_row)