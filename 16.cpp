// no need to remove duplicates!!!

#include <algorithm>
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int closest_target = nums[0] + nums[1] + nums[2];
        sort(nums.begin(), nums.end());
        int left, right;
        int sum;
        for(int i = 0; i < nums.size()-2;i++){
            left = i+1;
            right = nums.size()-1;
            while(left < right){
                sum = nums[i]+nums[left]+nums[right];
                // cout << "i: " << i << " left:" << left << "right:" << right << " sum: " << sum << '\n';
                // cout << "abs(target - sum): " << abs(target - sum) << " abs(closest_target - target): " << abs(closest_target - target) << '\n';
                closest_target = abs(target - sum) < abs(closest_target - target)?sum:closest_target;
                // if(closest_target == sum){
                //     cout << nums[i] << ' ' << nums[left] << ' ' << nums[right] << ' ' << sum << '\n'; 
                // }
                if(sum < target){
                    left++;
                }else if(sum > target){
                    right--;
                }else{
                    return target;
                }
            }
        }
        return closest_target;
    }
};
