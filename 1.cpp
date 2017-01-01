#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result;
        unordered_map<int,int> need;
        for(int i = 0; i < nums.size(); i++){
            if(need.find(target - nums[i]) != need.end()){
                cout << "find " << nums[i] << " match " << target - nums[i] << '\n';
                result.push_back(need[target - nums[i]]);
                result.push_back(i);
            }
            need.insert (make_pair(nums[i],i));
            cout << "insert:" << nums[i] << " at position " << i << '\n';
        }
        return result;
    }
};