# use a dictionary to store the groups, the key is the sorted string

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) <= 1:
            return [strs]
        dict = {}
        for str in strs:
            sorted_str = ''.join(sorted(str))
            if sorted_str in dict:
                dict[sorted_str].append(str)
            else:
                dict[sorted_str] = [str]
        result = []
        for key,value in dict.items():
            result.append(value)
        return result
