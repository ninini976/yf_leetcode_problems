#include <algorithm>    // std::sort
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int i = 0;
        int target;
        vector<vector<int>> result;
        sort(nums.begin(), nums.end());
        // for(;i < nums.size();i++){
        //     cout << nums[i] << ' ';
        // }
        // cout << '\n';
        for(;i < (int(nums.size())-2);i++){  // WARNING: nums.size()-2 will overflow if size is 0. since nums.size() has type unsigned int
            cout << "i:" << i << " nums[i]:" << nums[i] << '\n';
            target = -nums[i];
            int front = i+1;
            int back = nums.size()-1;
            while(front < back){
                //cout << "front: " << front << " back: " << back << '\n'; 
                if(nums[front] + nums[back] > target){
                    back--;
                }else if(nums[front] + nums[back] < target){
                    front++;
                }else{
                    vector<int> triple(3,0);
                    triple[0] = nums[i];
                    triple[1] = nums[front];
                    triple[2] = nums[back];
                    result.push_back(triple);
                    // handle duplicates for front
                    while(front+1 < nums.size() && nums[front] == nums[front+1]){
                        front++;
                    }
                    // handle duplicates for back
                    while(back-1 > i && nums[back] == nums[back-1]){
                        back--;
                    }
                    front++;
                    back--;
                }
            }
            // handle duplicate for the first number
            while(i < nums.size()-2 && nums[i] == nums[i+1]){
                i++;
            }
        }
        return result;
    }
};
