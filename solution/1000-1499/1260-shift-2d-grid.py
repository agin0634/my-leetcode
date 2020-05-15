class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m, n = len(grid), len(grid[0])
        if k < 1: return grid
        while k > 0:
            tmp = [[None]*n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if j == n-1:
                        last = grid[i][j]
                        if i < m-1:
                            tmp[i+1][0] = last
                        else:
                            tmp[0][0] = grid[m-1][n-1]
                    else:
                        tmp[i][j+1] = grid[i][j]
            k -= 1
            grid = tmp
        return tmp