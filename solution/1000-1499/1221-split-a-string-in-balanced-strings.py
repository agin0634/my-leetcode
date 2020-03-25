class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        res = 0
        for i in s:
            if not stack:
                res += 1
                
            if stack and stack[-1] != i:
                stack.pop()
            else:
                stack.append(i)
        return res