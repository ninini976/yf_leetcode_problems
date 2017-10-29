# corner case: k < 0
# corner case: k = 0
# two rounds to do this problem
# first create a num-freq map
# then check key-val pair one by one


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        map = {}
        paircount = 0
        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1
        
        for key,val in map.iteritems():
            if k == 0:
                if val > 1:
                    paircount += 1
            else:
                if key-k in map:
                    paircount += 1
                if key+k in map:
                    paircount += 1
        
        if k == 0:
            return paircount
        else:
            return paircount/2
