class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        c = collections.Counter(candies)
        if len(candies)/2 >= len(c):
            return len(c)
        else:
            return len(candies)/2