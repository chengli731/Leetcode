class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        if A == B:
            return True
        for i in range(1,len(A)):
            current = A[0:i] + B[0:len(A)-i]
            doublecheck = B[len(A)-i:len(A)]+A[i:len(A)]
            if current == A and doublecheck == A:
                return True
        return False
