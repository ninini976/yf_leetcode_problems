# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.L = nestedList
        self.idx = 0
        self.iter = None

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            if self.L[self.idx].isInteger():
                self.idx += 1
                # print("Get the interger %d" % self.L[self.idx-1].getInteger())
                self.iter = None
                return self.L[self.idx-1].getInteger()
            else:
                return self.iter.next()
        else:
            return None
                        

    def hasNext(self):
        """
        :rtype: bool
        """
        try:
            if self.L[self.idx].isInteger():
                return True
            else:
                if not self.iter: 
                    # find first iter.hasNext() == 1 or L[idx].isInteger() == 1
                    while True:
                        self.iter = NestedIterator(self.L[self.idx].getList())
                        if self.iter.hasNext():
                            return True
                        else:
                            self.idx += 1
                            if self.L[self.idx].isInteger():
                                self.iter = None
                                return True
                    
                else:
                    if self.iter.hasNext():
                        return True
                    else:
                        while True:
                            self.idx += 1
                            if self.L[self.idx].isInteger():
                                return True
                            else:
                                self.iter = NestedIterator(self.L[self.idx].getList())
                                if self.iter.hasNext():
                                    return True
        except Exception as error:
            return False
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
