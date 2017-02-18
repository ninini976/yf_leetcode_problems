# if a number is smaller than the number on its right, there must a peak on the right
# if a number is smaller that the number on its left, there must a peak on the left

# basic idea, using binary search

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left < right:
            mid = left + (right - left)/2
            
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid-1]: # if mid = 0, and the first condition is satisfied, will eventually return mid
                return mid
            
            if nums[mid] < nums[mid + 1]: # mid is not possible to be last idx of array
                left = mid+1
            else:
                right = mid-1
        return right
