class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #c = collections.Counter(nums)
        #return c.keys()[c.values().index(1)]
        
        dict = {}
        for n in nums:
            if n not in dict:
                dict[n] = 1
            else:
                dict[n] += 1
        return dict.keys()[dict.values().index(1)]