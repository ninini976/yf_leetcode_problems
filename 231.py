# right shift one bit at a time
# get the last bit
# see if it is 1
# if one, check the bit to the left
# corner case
# n = 0


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if not n:
            return False
        while True:
            bit = n & 1
            if bit == 1:
                n = n >> 1
                if n == 0:
                    return True
                else:
                    return False
            n = n >> 1
