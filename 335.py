# there are three types of cross
# 1. fourth cross the first, fifth cross second etc...

# ?????
# ?   ?
# ???????>
#     ?*


# 2. fifth meet first and so on

# ????
# ?  ?*
# ?  ?
# ????


# 3. sixth cross first

# ????
# ?  ??????
# ?       ?  
# ?????????


class Solution:
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        if len(x) <= 3:
            return False
        
        for i in range(3, len(x)):
            
            # fourth cross the first, fifth cross second etc...
            if x[i] >= x[i-2] and x[i-1] <= x[i-3]:
                return True
            
            # fifth meet the first and so on
            if i >= 4:
                # print(x[i-1], x[i-3])
                # print(x[i] + x[i-4], x[i-2])
                if x[i-1] == x[i-3] and x[i] + x[i-4] >= x[i-2]:
                    return True
                
            # sixth meet the first and so on
            if i >= 5:
                if x[i] + x[i-4] >= x[i-2] and x[i-1] + x[i-5] >= x[i-3] and x[i-1] <= x[i-3] and x[i-2] > x[i-4]:
                    return True
        
        return False
                    
                
