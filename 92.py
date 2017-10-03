# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# use a dummy node to refer to the node before head
# beg point to the current begin of reversed part
# end point to the current end of revesed part
# pre point to the node before the part to be reversed

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        for i in range(m-1):
            pre = pre.next
        end = pre.next
        beg = pre.next
        cur = end.next
        for i in range(n-m):
            #print('current:' , cur.val)
            next = cur.next
            cur.next = beg
            beg = cur
            cur = next
        pre.next = beg
        
        end.next = cur
        return dummy.next
            
        
