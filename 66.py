# corner case [9]
# need to return [1] on given []

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        if length == 0:
            return [1]
        if not digits[length-1] == 9:
            digits[length-1] += 1
            return digits
        else:
            return self.plusOne(digits[:-1]) + [0]
