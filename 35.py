class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        mid = left # handle corner case left == right
        while left < right:
            mid = left + (right - left)/2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        # WARNING: It is possible that (mid+1 = left= right)
        mid = left 
        if nums[mid] < target:
            return mid + 1
        else:
            return mid
