# use depth first search algorithm for this problem
# dfs(nums, sums, index, target)



class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 4:
            return False
        sum = 0
        for num in nums:
            sum += num
        if not sum % 4 == 0:
            return False
        # create four bins to put the numbers in
        sums = [0]*4
        target = sum / 4
        # reverse sort allow put longest matches in to bins first
        nums.sort(reverse=True)
        
        def dfs(nums, sums, index, target):
            if index == len(nums):
                if sums[0] == target and sums[1] == target and sums[2] == target and sums[3] == target:
                    return True
                else:
                    return False
            # put the number at index into each bin and see if it fits
            for i in range(4):
                if nums[index] + sums[i] > target:
                    continue
                # this is sort of depth first search + recursion
                sums[i] += nums[index]
                if (dfs(nums, sums, index+1, target)):
                    return True
                sums[i] -= nums[index]
            
            return False
                
        
        return dfs(nums, sums, 0, sum/4)
