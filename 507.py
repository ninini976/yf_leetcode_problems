# edge case: num < 0, num = 1
# sqrt: int(math.sqrt())

class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        sum = 0
        sqrt = int(math.sqrt(num))
        
        for i in range(1,sqrt+1):
            if num%i == 0:
                sum += i
                sum += num/i
        if sqrt*2 == num:
            sum -= sqrt
        return sum == 2*num
