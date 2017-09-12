# iterative and recursive solution are easy to come up with
# this is a solution without loops


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 1162261467 is 3^19 it is the max power of 3 that falls in int
        # this method only works for porwer of prime number
        return n > 0 and 1162261467%n == 0
