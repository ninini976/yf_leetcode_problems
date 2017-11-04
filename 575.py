# return number of kinds or 
# half the size of array


class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        cset = set()
        kindCount = 0
        for c in candies:
            if not c in cset:
                cset.add(c)
                kindCount += 1
        return kindCount if kindCount < len(candies)/2 else len(candies)/2
