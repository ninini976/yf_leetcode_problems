# two instance var
# self.stack = []
# self.minval
# sys.maxint
# del self.stack[-1]

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minval = sys.maxint
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        self.minval = min(x,self.minval)

    def pop(self):
        """
        :rtype: void
        """
        if self.stack[-1] == self.minval:
            del self.stack[-1]
            if self.stack:
                self.minval = min(self.stack)
            else:
                self.minval = sys.maxint
        else:
            del self.stack[-1]
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minval


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
