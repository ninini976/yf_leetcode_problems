class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(32):
            count += 1 & n
            n = n >> 1
        return count
