# two counters and two candidates
# Boyer-Moore Majority Vote algorithm

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        c1,c2,count1,count2 = 0,0,0,0
        for n in nums:
            #print(c1,c2,count1,count2)
            # must do n == c1? n == c2 first
            # must increment the counter if possible first
            if n == c1:
                count1 += 1
            elif n == c2:
                count2 += 1
            elif count1 == 0:
                c1 = n
                count1 = 1
            elif count2 == 0:
                c2 = n
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        res = []
        print(c1,c2)
        if nums.count(c1) > len(nums) // 3:
            res.append(c1)
        if c1 != c2 and nums.count(c2) > len(nums) // 3:
            res.append(c2)
        return res
