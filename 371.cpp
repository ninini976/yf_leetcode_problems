# (a&b)<<1 find the carry
# a^b get the sum without all carries


class Solution {
public:
    int getSum(int a, int b) {
        return b==0?a:getSum(a^b,(a&b)<<1);
    }
};
