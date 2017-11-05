class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        lowerBound = int(math.ceil(float(len(B))/len(A)))
        if B in A*lowerBound:
            return lowerBound
        if B in A*(lowerBound+1):
            return lowerBound+1
        return -1
