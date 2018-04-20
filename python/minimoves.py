class Solution:
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mymedian = self.median(nums)
        step  = 0
        for x in range(len(nums)):
            step = abs(nums[x]-mymedian)+step
        
        return step
            
    def median(self,myarray):
        myarray = sorted(myarray)
        if len(myarray)%2 ==0:
            return myarray[round(len(myarray)/2-1)]
        else:
            return myarray[round((len(myarray)+1)/2 -1)]
