# easy
# iterate from 1 to sqrt(c)
# put square numbers in set

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        squares = set()
        for i in range(int(c**0.5)+1):
            squares.add(i*i)
            if c - i*i in squares:
                return True
        return False
