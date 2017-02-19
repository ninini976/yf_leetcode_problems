class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        idxa = len(a) - 1
        idxb = len(b) - 1
        carry = 0
        result = ""
        while idxa > -1 or idxb > -1 or carry:
            numa = int(a[idxa]) if idxa > -1 else 0
            numb = int(b[idxb]) if idxb > -1 else 0
            carry = numa + numb + carry
            result = str(carry%2) + result
            idxa -= 1
            idxb -= 1
            carry /= 2
        return result
