class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for num in nums:
            # i < 2 set up the first two numbers no metter what they are
            if i < 2 or num > nums[i-2]:
                nums[i] = num
                i += 1
        return i
