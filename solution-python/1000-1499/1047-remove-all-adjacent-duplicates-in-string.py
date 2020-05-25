class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        
        for i in S:
            if stack:
                if stack[-1] == i:
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        return "".join(stack)