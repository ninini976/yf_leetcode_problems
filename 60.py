# recursive method
# get the first digit, then modify the number list, remainer of k and loop length


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        
        number_list = [str(i+1) for i in range(n)]
        divide_number = math.factorial(n-1)
        
        
        def permhelper(number_list, divide_number, s, k):
            if len(number_list) == 1:
                return s+number_list[0]
            
            idx = int(math.ceil(1.0*k / divide_number)-1)
            remainer = k - k/divide_number*divide_number
            
            s = s + number_list[idx]
            del number_list[idx]
            
            return permhelper(number_list, divide_number/len(number_list), s, remainer)
            
        return permhelper(number_list, divide_number, "", k)
