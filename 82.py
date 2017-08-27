# BEST easy way to do this problem: recursion!

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
            return None
        next = head.next
        if next:
            if next.val != head.val:
                head.next = self.deleteDuplicates(head.next)
                return head
            else:
                while next:
                    next = next.next
                    if not next:
                        return None
                    if next.val != head.val:
                        return self.deleteDuplicates(next)
        else:
            return head
