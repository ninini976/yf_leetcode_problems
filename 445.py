# implement using two stacks
# put everything in the singly linked list into two stacks
# pop one from each stack and add using while loop. balabala


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
            
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        
        sum = 0
        head = None
        while len(stack1) or len(stack2):
            if not len(stack1):
                sum += stack2.pop()
            elif not len(stack2):
                sum += stack1.pop()
            else:
                sum += stack1.pop() + stack2.pop()
            
            dig = sum % 10
            current = ListNode(dig)
            current.next = head
            head = current
            sum = sum/10
        if sum:
            current = ListNode(sum)
            current.next = head
            head = current
        return head
