# the order when dealing with move around mmm,mm,m is very important and easy to make mistake on
# to update mmm
# m = mm
# mm = mmm
# mmm = num
# from bottom to up

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = -sys.maxint - 1
        mm = -sys.maxint - 1
        mmm = -sys.maxint - 1
        for num in nums:
            if num > mmm:
                # must keep this order!
                m = mm
                mm = mmm
                mmm = num
                continue
            if num < mmm and num > mm:
                m = mm
                mm = num
                continue
            if num < mm and num > m:
                m = num
                continue
        res = -sys.maxint - 1
        if m != -sys.maxint - 1:
            res = m
        else:
            res = mmm
        return res
