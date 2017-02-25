###
Given a string, find the length of the longest substring T that contains at most k distinct characters.

For example, Given s = “eceba” and k = 2,

T is "ece" which its length is 3.
###

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # use a dictionary to keep track of char, pos pair, record the right most postion of letter
        dict = {}
        longest = 0
        start = 0
        end = 0
        distinct = 0
        while not end == len(s):
            if s[end] not in dict:
                dict[s[end]] = end
                end += 1
                distinct += 1
            elif dict[s[end]] < start:
                dict[s[end]] = end
                end += 1
                distinct += 1
            else: # dict[s[end]] >= start
                dict[s[end]] = end
                end += 1
            while distinct > k:
                if dict[s[start]] == start:
                    distinct -= 1
                    start += 1
                else:
                    start += 1
            # print(start,end)
            longest = end - start if end - start > longest else longest
            # print(longest)
        #return len(s[longest[0]:longest[1]])
        return longest
