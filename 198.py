# recursive relation
# f(0) = nums[0]
# f(1) = max(nums[0, nums1)
# f(k) = max(f(k-2) + nums[k], f(k-1))
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre = 0
        cur = 0
        for i in range(len(nums)):
            tmp = pre
            pre = cur
            cur = max(tmp+nums[i], cur)
        return cur
