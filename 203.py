# Good approach. Use dummy node
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        head, head.next = ListNode(0), head
        pre = head
        cur = head.next
        while cur:
            #print(cur.val)
            if cur.val == val:
                cur = cur.next
                pre.next = cur
            else:
                pre.next = cur
                pre = cur
                cur = cur.next
        return head.next




# BAD: recursive solution, reach recurion limit

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None
        head.next = self.removeElements(head.next,val)
        if head.val == val:
            return head.next
        else:
            return head
