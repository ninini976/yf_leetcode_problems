# as many 3s as possible when larger than 4
# 2*2*2 < 3*3
# we can always replace three 2s with two 3s


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        product = 1
        while n > 4:
            product *= 3
            n -= 3
        product *= n
        return product
