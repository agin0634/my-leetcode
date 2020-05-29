class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i,e in enumerate(numbers):
            other = target - e
            if other in dict:
                return[dict[other], i+1]
            else:
                dict[e] = i+1