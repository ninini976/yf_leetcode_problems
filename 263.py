# recursion depth too large
# handle corner case num = 0


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if not num:
            return False
        while True:
            if num == 1:
                return True
            else:
                if num % 2 == 0:
                    num /= 2
                    continue
                if num % 3 == 0:
                    num /= 3
                    continue
                if num % 5 == 0:
                    num /=5
                    continue
                return False
