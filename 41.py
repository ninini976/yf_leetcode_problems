class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # no number, return 1
        if not nums:
            return 1
        
        for i in range(len(nums)):
            # very important here, to put every number at the right place 
            # use WHILE to keep swaping
            # avoid swaping two same number
            # get the index first than swap
            while nums[i] > 0 and nums[i] < len(nums) and nums[i] != i+1 and nums[nums[i]-1] != nums[i]:
                #print(i, nums[i]-1)
                idx0 = nums[i]-1
                idx1 = i
                nums[idx0], nums[idx1] = nums[idx1], nums[idx0]
        
        #print(nums)
        
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        
        # all in right place, return last one + 1
        return nums[-1]+1
