# use recursion to find next
# not very hard

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        start = '1'
        for i in range(n-1):
            start = self.next(start)
        return start
        
        
    def next(self, string):
        if string == '':
            return ''
        i = 1
        while i < len(string):
            if string[i] == string[0]:
                i += 1
            else:
                break
        return str(i)+string[0]+self.next(string[i:])
