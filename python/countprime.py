class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        Pcount = [1]*(n+1)
        Pcount[0] = 0
        Pcount[1] = 0
        k = 2
        while k^2 <= n:
            if Pcount[k] == 1:
                j = k
                while k*j <= n:
                    Pcount[k*j] = 0
                    j+=1
            k+=1
        return sum(Pcount)
