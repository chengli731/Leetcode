class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.item = []
        self.min = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.item.append(x)
        if not self.min or x<self.min[-1]:
            self.min.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.min and self.item[-1] == self.min[-1]:
            del self.min[-1]
        del self.item[-1]

    def top(self):
        """
        :rtype: int
        """
        return self.item[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.min:
            return self.min[-1]
        else:
            return None
