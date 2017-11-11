# 3 pointers
# first pointer swep from nums[0] to nums[-3] use for loop
#       left = i+1, right = nums[-1]


class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count = 0
        nums = sorted(nums)
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            while left < right:
                # we good now, count += right - left
                if nums[i] + nums[left] + nums[right] < target:
                    count += right - left
                    left += 1
                # we not good, move right towards left
                else:
                    right -= 1
                    
        return count
