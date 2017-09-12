# sum([int(x)**2 for x in str(slow)]) give sum of digits square
# slow and fast detect loop



class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        fast = slow = n
        while True:
            slow = sum([int(x) **2 for x in str(slow)])
            fast = sum([int(x) **2 for x in str(fast)])
            fast = sum([int(x) **2 for x in str(fast)])
            if fast == 1:
                return True
            if slow == fast:
                break
        return slow == 1
