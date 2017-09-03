# very interesting dp solution with interesting dp relation
# dp[i] is maxsubarray sum of nums[:i+1] which MUST contain nums[i]
# dp[i+1] = dp[i]<0 ? nums[i+1] : nums[i+1] + dp[i]
# ans = max(dp)


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []
        dp.append(nums[0])
        for i in range(len(nums)-1):
            if dp[i] <= 0:
                dp.append(nums[i+1])
            else:
                dp.append(nums[i+1]+dp[i])
        return max(dp)
