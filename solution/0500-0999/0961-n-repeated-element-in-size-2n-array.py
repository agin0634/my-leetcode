class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dict = {}
        for a in A:
            if a not in dict:
                dict[a] = 1
            else:
                dict[a] += 1
        return dict.keys()[dict.values().index(len(A)/2)]