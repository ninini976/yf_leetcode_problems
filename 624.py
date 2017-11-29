class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        diff = 0
        minnum = arrays[0][0]
        maxnum = arrays[0][-1]
        
        # loop must start from 1 to avoid use same head and tail from same array
        for i in range(1, len(arrays)):
            nums = arrays[i]
            head = nums[0]
            tail = nums[-1]
            # This can prevent using head and tail from same array
            diff = max(diff, abs(tail - minnum))
            diff = max(diff, abs(maxnum - head))
            maxnum = max(maxnum, tail)
            minnum = min(minnum, head)
            
        return diff
