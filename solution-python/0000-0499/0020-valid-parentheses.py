class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }
        
        stack = []
        
        for c in s:
            if c in dict:
                stack.append(c)
            elif stack:
                if dict[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
            else:
                return False
        return len(stack) == 0