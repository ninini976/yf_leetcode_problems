# corner cases to consider 
# "Z"
# "AZ"

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if n <= 26:
            return letters[n-1]
        else:
            return self.convertToTitle((n-1)/26) + letters[n%26 - 1]
