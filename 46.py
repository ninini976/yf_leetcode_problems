class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [[nums[0]]]
        result = []
        for i in range(len(nums)):
            head = nums[i]
            lrest = self.permute(nums[:i]+nums[i+1:])
            for l in lrest:
                result.append([head]+l)
        return result
