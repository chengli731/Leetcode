class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        self.comb(1,n,k,ans,[])
        return ans
    
    def comb(self,start,n,k,ans,r):
        if not k:
            ans.append(r)
            return
        for i in range(start,n+1):
            self.comb(i+1,n,k-1,ans,[i]+r)
