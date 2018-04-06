class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        numslen = len(nums)-1
        ans = []
        if nums is None:
            return []
        else:
            self.recurpermute(nums,0,numslen,ans)
            
        return ans
        
    def recurpermute(self, a, l, r,ans):
        if l == r:
            c = a[:]
            ans.append(c)
        else:
            for i in range(l,r+1):
                a[l],a[i]=a[i],a[l]
                self.recurpermute(a,l+1,r,ans)
                a[l],a[i]=a[i],a[l]
