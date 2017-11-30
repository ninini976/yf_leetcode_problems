class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2): 
            return False
        # map: apply function to all elements in array
        # build set of all pairs
        pairset = set(map(tuple, pairs))
        
        # print(pairset)
        
        for i in range(len(words2)):
            # same words or any of the order in pairset
            if words1[i] == words2[i] or ((words1[i], words2[i]) in pairset) or ((words2[i], words1[i]) in pairset):
                continue
            else:
                return False
            
        return True
