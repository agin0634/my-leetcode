class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        ans = [0] * num_people
        count,i = 1,0
        while candies:
            if count < candies:
                ans[i] += count
                candies -= count
                count += 1
            else:
                ans[i] += candies
                break
            if i == num_people - 1:
                i = 0
            else:
                i += 1
        return ans