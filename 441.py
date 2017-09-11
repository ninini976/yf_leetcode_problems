# math solution
# math.floor
# (1+8*n)**(1/2.0)

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.floor((-1+(1+8*n)**(1/2.0))/2.0))
