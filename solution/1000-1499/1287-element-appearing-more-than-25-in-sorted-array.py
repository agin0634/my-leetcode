class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        t = len(arr) * 0.25
        curr,c = 0,1
        for a in arr:
            if a == curr:
                c += 1
                if c > t:
                    return curr
            else:
                c = 0
                curr = a
        return curr