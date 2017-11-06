# corner case: [1]
# series of 1s as ending 

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        max_count = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
            if num == 0:
                max_count = max(count, max_count)
                count = 0
        max_count = max(count, max_count)
        return max_count
