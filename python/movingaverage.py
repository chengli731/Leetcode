class MovingAvergae(object):
    def __init__(self,size):
        #initialize data structure
        #size is an integer
        self.size = size
        self.q = []
        self.windowsum = 0


    def next(self,val):
        if len(self.q) >= self.size:
            self.q.pop()
        self.q.insert(0,val)
        self.windowsum = sum(self.q)

        return self.windowsum/len(self.q)
        
        
