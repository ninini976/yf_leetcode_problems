# num&num-1 == 0 make sure there is only one bit '1' in the binary number
# num&int('55555555',16) != 0 make sure that the only bit '1' must occur on even position

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and num&(num-1) == 0 and num&int('55555555',16)!=0
