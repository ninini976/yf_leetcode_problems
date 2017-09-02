# use a dummy list head
# solve the problem quick and clean

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        tail = dummy
        while l1 and l2:
            #print('l1',l1.val,'l2',l2.val)
            if l1.val < l2.val:
                tail.next = l1
                tail = l1
                l1 = l1.next
            else:
                tail.next = l2
                tail = l2
                l2 = l2.next
        if l1:
            tail.next = l1
        else:
            tail.next = l2
        return dummy.next
