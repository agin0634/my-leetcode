class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        dict, res = {}, -1
        for i in arr:
            dict[i] = dict.get(i,0) + 1
        for k,i in dict.items():
            if k == i:
                res = i
        return res