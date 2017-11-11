# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head

        len = 0
        cur = head
        # get the length of linked list
        while cur:
            len += 1
            cur = cur.next
            
        k = k % len
        
        # k is 0, just return head
        if not k:
            return head
        
        # find newtail and cur tail
        newtail = head
        tail = head
        # rotate k length, dist between new tail and tail is k
        # example k = 1
        for i in range(k):
            tail = tail.next
            
        while tail.next:
            tail = tail.next
            newtail = newtail.next
        
        tail.next = head
        head = newtail.next
        newtail.next = None
        
        return head
