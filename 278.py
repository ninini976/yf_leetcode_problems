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
        while left < right: # the terminate condition for this while statement can only be left == right.
            mid = left + (right - left)/2
            if not isBadVersion(mid):
                left = mid+1 # this garantee left will increase at least one if mid is good
            else:
                right = mid # this will make sure that right is always point to a bad version
        return left
    
   
