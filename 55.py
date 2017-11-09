# iterate and update max jump reach

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reach = 0
        for i in range(len(nums)):
            print(i, reach)
            if reach < i:
                return False
            if reach >= len(nums) - 1:
                return True
            reach = max(i+nums[i], reach)
        return True
