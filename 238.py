# If there are four elements in the array
# An explanation of polygenelubricants method is: The trick is to construct the arrays (in the case for 4 elements)

# {              1,         a[0],    a[0]*a[1],    a[0]*a[1]*a[2],  }
# { a[1]*a[2]*a[3],    a[2]*a[3],         a[3],                 1,  }


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        res.append(1)
        
        for i in range(1,len(nums)):
            res.append(res[-1]*nums[i-1])
        
        # print(res)
        # p here is use to "construct" the second array
        p = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] = res[i] * p
            p = p * nums[i]
            
        return res
