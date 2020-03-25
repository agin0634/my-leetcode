class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.currentMin = float("inf")

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        
        if x < self.currentMin:
            self.currentMin = x

    def pop(self):
        """
        :rtype: None
        """
        del self.stack[-1]
        
        if self.stack:
            self.currentMin = min(self.stack)
        else:
            self.currentMin = float("inf")
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.currentMin


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()