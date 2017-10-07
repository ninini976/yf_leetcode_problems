# use bucket
# keep at most k buckets
# interesting way to do range check


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # use bucket to store numbers within a range
        # keep at most k buckets
        if t < 0:
            return False
        w = t + 1
        bucket = {}
        for i in range(len(nums)):
            b_idx = nums[i]/w
            print(nums[i], b_idx)
            if b_idx in bucket:
                return True
            if b_idx + 1 in bucket and abs(nums[i] - bucket[b_idx + 1]) < w:
                return True
            if b_idx - 1 in bucket and abs(nums[i] - bucket[b_idx - 1]) < w:
                return True
            bucket[b_idx] = nums[i]
            if i >= k:
                del bucket[nums[i-k]/w]
        return False
