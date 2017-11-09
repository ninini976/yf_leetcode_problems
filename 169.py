class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # # random algorithm
        # while(True):
        #     candidate = random.randint(0,len(nums)-1)
        #     count = 0
        #     for num in nums:
        #         if num == nums[candidate]:
        #             count += 1
        #     if count >= len(nums)/2.0:
        #         return nums[candidate]
        
        # Boyer-Moore Majority Vote Algorithm
        count = 0
        mj = 0
        for num in nums:
            if count == 0:
                mj = num
            if num == mj:
                count += 1
            else:
                count -= 1
        # this is a process of varification, can throw away if a mj is garanteed
        count = 0
        for num in nums:
            if num == mj:
                count += 1
        
        return mj 
