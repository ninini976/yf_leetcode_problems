# helper data structure sums[]
# sumRange(i,j) = sums[j] - sums[i]


class NumArray(object):
    
    sums = []

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if not nums:
            return 
        self.sums = [nums[0]]
        for i in range(len(nums) - 1):
            self.sums.append(self.sums[-1] + nums[i+1])
            

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i != 0:
            return self.sums[j] - self.sums[i-1]
        else:
            return self.sums[j]
        
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
