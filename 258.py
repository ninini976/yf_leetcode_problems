# num:  0 1 2 3 4 5 6 7 8 9 10 11 12 13 ...
# res:  0 1 2 3 4 5 6 7 8 9 1 2 3 4 ... 


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        else:
            return (num-1)%9+1
