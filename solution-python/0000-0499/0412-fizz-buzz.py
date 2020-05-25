class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in range(1,n+1):
            w = ''
            if i % 3 == 0:
                w += 'Fizz'
            if i % 5 == 0:
                w += 'Buzz'
            if w:
                res.append(w)
            else:
                res.append(str(i))
        return res