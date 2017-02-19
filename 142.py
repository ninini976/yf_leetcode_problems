# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        try:
            # start from head, idx1 move one step each time, idx2 move two steps each time
            idx1 = head.next
            idx2 = head.next.next
            while not idx1 == idx2:
                idx1 = idx1.next
                idx2 = idx2.next.next
            idx3 = head
            while not idx3 == idx2:
                idx2 = idx2.next
                idx3 = idx3.next
            return idx3
        except:
            return None
