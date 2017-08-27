# two sets

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        sequence_set = set()
        repeated_set = set()
        if len(s) < 10:
            return list(sequence_set)
        for i in range(0,len(s)-9):
            if s[i:i+10] in sequence_set:
                repeated_set.add(s[i:i+10])
                continue
            else:
                sequence_set.add(s[i:i+10])
        return list(repeated_set)
