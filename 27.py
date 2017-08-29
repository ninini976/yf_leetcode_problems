# not hard, interesting problem
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        begin = 0
        for num in nums:
            if num != val:
                nums[begin] = num
                begin += 1
        return begin
