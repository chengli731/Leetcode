class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.item = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.item.append(x)

    def pop(self):
        """
        :rtype: void
        """
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
        return min(self.item)

