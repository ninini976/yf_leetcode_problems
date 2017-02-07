// xor: 0 0 -> 0; 0 1 -> 1; 1 0 -> 1; 1 1 ->0
// ^= use bit operation, same number with result in 0
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int result = 0;
        for(int i = 0; i < nums.size(); i++){
            result ^= nums[i];
        }
        return result;
    }
};
