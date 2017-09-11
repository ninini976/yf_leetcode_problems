# a very interesting random algorithm solution


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while(True):
            candidate = random.randint(0,len(nums)-1)
            count = 0
            for num in nums:
                if num == nums[candidate]:
                    count += 1
            if count >= len(nums)/2.0:
                return nums[candidate]
