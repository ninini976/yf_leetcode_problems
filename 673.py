# len[i]: the length of the Longest Increasing Subsequence which ends with nums[i].
# cnt[i]: the number of the Longest Increasing Subsequence which ends with nums[i].
# initial
# len[0] = 1
# cnt[0] = 1
# len[i+1] = max([len[k]+1  for k in range(i) if nums[k] < nums[i+1]])
# cnt[i+1] = cnt[k] + 1 (k is the index for max length)
class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # corner case
        if not nums:
            return 0
        
        lens = []
        cnt = []
        lens.append(1)
        cnt.append(1)
        for i in range(len(nums)-1):
            
            max_len = -1
            max_idx = -1
            for j in range(i+1):
                if nums[j] < nums[i+1]:
                    if lens[j] > max_len:
                        max_len = lens[j]
                        max_idx = j
            if max_len != -1:
                lens.append(max_len+1)
                cnt.append(sum([cnt[k] for k in range(i+1) if lens[k] == max_len and nums[k] < nums[i+1]]))
            else:
                lens.append(1)
                cnt.append(1)
        
        # print(lens)
        # print(cnt)
        
        return sum([cnt[i] for i in range(len(cnt)) if lens[i] == max(lens)])
