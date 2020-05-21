class Solution(object):
    table = {0:0, 1:1}
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N in self.table: return self.table[N]
        self.table[N] = self.fib(N-1) + self.fib(N-2)
        return self.table[N]