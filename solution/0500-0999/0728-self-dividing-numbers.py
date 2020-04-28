class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for i in range(left,right+1):
            s = str(i)
            isSelfDivid = True
            for c in s:
                if int(c) == 0:
                    isSelfDivid = False
                    break
                elif i % int(c) != 0:
                    isSelfDivid = False
            if isSelfDivid:
                res.append(i)
        return res