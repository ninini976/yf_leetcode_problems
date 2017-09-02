# fill in the array nums1 from back to front
# k is back idx in nums1
# i is idx in nums1
# j is idx in nums2


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        k = m + n - 1
        i = m - 1
        j = n - 1
        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
        # no need for these two lines, only help understanding
        # if i >= 0:
        #     nums1[:i] = nums1[:i]
        if j >= 0:
            nums1[:j+1] = nums2[:j+1]
