class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for i in range(rowIndex):
            # https://leetcode.com/problems/pascals-triangle-ii/discuss/306320/An-O(k)-solution-with-explanation
            row.append((row[i] * (rowIndex - i)) // (i + 1))
        return row