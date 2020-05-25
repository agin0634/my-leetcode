class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        
        for i in S:
            if stack and i == ")" and stack[-1] != i:
                stack.pop()
            else:
                stack.append(i)
        return len(stack)