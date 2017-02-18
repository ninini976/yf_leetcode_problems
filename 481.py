class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n <= 3:
            return 1
        s = [0 for _ in range(n)]
        s[0] = 1
        s[1] = 2
        s[2] = 2
        upidx = 3
        downidx = 1
        result = 1
        remain = 0
        num_fill = 0
        while upidx < n:
            if remain == 0:
                downidx += 1
                num_fill = s[upidx-1] ^ 3
                remain = s[downidx]
            s[upidx] = num_fill
            upidx += 1
            remain -= 1
            if num_fill == 1:
                result += 1
        return result
