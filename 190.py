# straightforward solution
# get the last bit
# shift n to right by 1
# add to result

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            bit = n & 1
            res += bit * 2 ** (32-i-1)
            n = n >> 1
        return res
