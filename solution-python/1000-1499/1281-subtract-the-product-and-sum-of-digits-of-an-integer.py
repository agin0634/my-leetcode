class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        pro, sum = 1 ,0
        while n > 0:
            i = n % 10
            n /= 10
            pro *= i
            sum += i
        return pro - sum