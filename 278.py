# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while True:
            mid = left + (right - left)/2
            if mid == left:
                if isBadVersion(mid):
                    return mid
                else:
                    return mid+1
            if not isBadVersion(mid):
                left = mid
            else:
                right = mid
