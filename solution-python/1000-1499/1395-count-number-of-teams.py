class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(rating)-2):
            for j in range(i+1, len(rating)):
                if rating[j] > rating[i]:
                    for k in range(j+1, len(rating)):
                        if rating[k] > rating[j]:
                            res += 1
                else:
                    for k in range(j+1, len(rating)):
                        if rating[k] < rating[j]:
                            res += 1
        return res