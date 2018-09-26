class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        dict1 = {}
        dict2 = {}
        for c in s:
            if c in dict1:
                dict1[c] += 1
            else:
                dict1[c] = 1
        for c in t:
            if c in dict2:
                dict2[c] += 1
            else:
                dict2[c] = 1
        for key, value in dict1.iteritems():
            if not key in dict2:
                return False
            if dict2[key] != value:
                return False
        return True
