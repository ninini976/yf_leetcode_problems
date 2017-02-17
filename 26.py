# do not use del nums[i] since it is a O(n) operation
# only need the first len numbers to be unique, no need to remove duplicates from list
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        newtail = 0
        for i in range(1,len(nums)):
            if nums[i] == nums[newtail]:
                continue
            else:
                nums[newtail+1] = nums[i]
                newtail += 1
        return newtail+1
