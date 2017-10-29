# python sort tuple based on second element
# numlist.sort(key=operator.itemgetter(1),reverse=True)

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nummap = {}
        numlist = []
        for num in nums:
            if num in nummap:
                nummap[num] += 1
            else:
                nummap[num] = 1
        for key, value in nummap.iteritems():
            numlist.append((key,value))
        numlist.sort(key=operator.itemgetter(1),reverse=True)
        return [numlist[i][0] for i in range(k)] 
