# only need 2 pointers. current & next

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        current = head
        next = head.next
        while next:
            if current.val == next.val:
                next = next.next
                current.next = next
            else:
                current = next
                next = next.next
        return head
