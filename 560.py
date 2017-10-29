# sum[i,j] = sum[0,j] - sum[0,i]
# for j = 0,n
# sum = sum[0,j]
# check if sum-k is in map
# put sum into map(frequency map)


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        map = {}
        # 0 number add is 0
        map[0] = 1
        sum = 0
        count = 0
        for num in nums:
            sum += num
            # check and add counter first
            if (sum - k) in map:
                count += map[sum-k]
            
            # then add current sum into map
            if sum in map:
                map[sum] += 1
            else:
                map[sum] = 1
        
        return count
                
