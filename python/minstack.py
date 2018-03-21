class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        self.min = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.items.append(x)
        if not self.min or x<self.min[-1]:
            self.min.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.min and self.items[-1] == self.min[-1]:
            self.min.pop()
        if self.items:
            self.items.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.items[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.min:
            return self.min[-1]
        else:
            return None
