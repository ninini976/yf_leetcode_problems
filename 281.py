'''
Given two 1d vectors, implement an iterator to return their elements alternately.

For example, given two 1d vectors:

v1 = [1, 2]
v2 = [3, 4, 5, 6]
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].

Follow up: What if you are given k 1d vectors? How well can your code be extended to such cases?

Clarification for the follow up question - Update (2015-09-18):
The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For example, given the following input:

[1,2,3]
[4,5,6,7]
[8,9]
It should return [1,4,8,2,5,9,3,6,7]
'''

# data structure used: self.pointers record pointers on each list (initialized to be both -1)
# self.pl record which list we are looking at

# hasNext() do: check if there is next, adjust pointers on to next pointer
# next() do: get the number from a valid pointer, then change self.pl to next list

class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.list = [v1,v2]
        self.pointer = [-1,-1]
        self.pl = 0
        
    def next(self):
        """
        :rtype: int
        """
        res = self.list[self.pl][self.pointer[self.pl]]
        self.pl = ~self.pl
        return res
        

    def hasNext(self):
        """
        :rtype: bool
        """
        # print(self.list, self.pointer, self.pl)
        # increment a pointer
        self.pointer[self.pl] += 1
        # check if in bound
        if self.pointer[self.pl] < len(self.list[self.pl]):
            return True
        else:
            self.pl = ~self.pl
            # increment the other pointer
            self.pointer[self.pl] += 1
            # check in bound
            if self.pointer[self.pl] < len(self.list[self.pl]):
                return True
            else:
                return False

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())

# an very concise answer from StefanPochmann
'''
 public class ZigzagIterator {

    private Iterator<Integer> i, j, tmp;

    public ZigzagIterator(List<Integer> v1, List<Integer> v2) {
        i = v2.iterator();
        j = v1.iterator();
    }

    public int next() {
        if (j.hasNext()) { tmp = j; j = i; i = tmp; }
        return i.next();
    }

    public boolean hasNext() {
        return i.hasNext() || j.hasNext();
    }
}
'''



