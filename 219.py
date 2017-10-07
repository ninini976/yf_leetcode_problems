# map from a number to a list of indexs

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        numset = {}
        for i in range(len(nums)):
            if nums[i] not in numset:
                numset[nums[i]] = [i]
            else:
                for j in range(len(numset[nums[i]])):
                    if abs(i-numset[nums[i]][j]) <= k:
                        return True
                numset[nums[i]].append(i)
            #print(numset)
        return False
