# two priority queues
# max and min

import heapq

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heaps = [],[]
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        small, large = self.heaps
        # throw num into large, get one from large and throw into small
        elem = -heapq.heappushpop(large, num)
        heapq.heappush(small, elem)
        # adjust len of two heaps
        if len(small) > len(large):
            elem = heapq.heappop(small)
            heapq.heappush(large, -elem)
        
        # print(small, large)
        
    def findMedian(self):
        """
        :rtype: float
        """
        small, large = self.heaps
        if len(large) != len(small):
            return large[0]
        else:
            return (-small[0]+large[0])/2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
