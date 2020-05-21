class Solution(object):
    table = {}
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n ==1:
            self.table[n] = 1
            return self.table[n]
        if n in self.table:
            return self.table[n]
        self.table[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.table[n]