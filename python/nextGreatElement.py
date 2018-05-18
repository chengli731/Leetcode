class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d,stack,myresult = {},[],[]
        for x in nums2:
            while(len(stack) and x>stack[-1]):
                premax = stack.pop()
                d[premax] = x
            stack.append(x)
        
        for y in stack:
            d[y] = -1
        
        for i in range(len(nums1)):
            myresult.append(d[nums1[i]])
            
