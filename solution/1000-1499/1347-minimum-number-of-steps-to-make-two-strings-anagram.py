class Solution(object):
    def minSteps(self, s, t):
        return sum((collections.Counter(s) - collections.Counter(t)).values())
        
        