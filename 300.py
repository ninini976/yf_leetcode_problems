# maintain an array tails
# tails[i] is the smallest tail of all increasing subsequences of length = i+1 in nums
# it is a increasing array (easily prove)
# bulid/update the array tail while we iterate through the nums array
# binary search get 


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tail = []
        for num in nums:
            l = 0
            r = len(tail)
            while l != r:
                m = (l+r)/2
                if tail[m] >= num:
                    r = m
                    continue
                if tail[m] < num:
                    l = m + 1
                    continue
            # in this binary search l is the index that tail[l] >= num
            # num is largest among tail, append
            if l == len(tail):
                tail.append(num)
            # num <= tail[l], update tail[l]
            else:
                tail[l] = num
        return len(tail)
