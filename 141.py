# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# idea is simple
# the tricky way to make the function faster is to use except to catch excptions and return false

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        try:
            idx1 = head
            idx2 = head.next
            while not idx1 == idx2:
                idx1 = idx1.next
                idx2 = idx2.next.next
            return True
        except:
            return False
                
