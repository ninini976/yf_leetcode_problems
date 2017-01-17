class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> result;
        if(nums.size() < 4){
            return result;
        }
        sort(nums.begin(), nums.end());
        int first, second, third, fourth;
        for(first = 0; first < nums.size()-3; first++){
            int threesum = target - nums[first];
            for(second = first+1; second < nums.size()-2; second++){
                int twosum = threesum - nums[second];
                third = second + 1;
                fourth = nums.size() - 1;
                while(third < fourth){
                    if(nums[third] + nums[fourth] > twosum){
                        fourth--;
                    }else if(nums[third] + nums[fourth] < twosum){
                        third++;
                    }else{
                        vector<int> temp;
                        temp.push_back(nums[first]);
                        temp.push_back(nums[second]);
                        temp.push_back(nums[third]);
                        temp.push_back(nums[fourth]);
                        result.push_back(temp);
                        while(third+1 < nums.size() && nums[third] == nums[third+1]){
                            third++;
                        }
                        third++;
                        while(fourth-1 >= 0 && nums[fourth] == nums[fourth-1]){
                            fourth--;
                        }
                        fourth--;
                    }
                }
                while(second+1 < nums.size() && nums[second] == nums[second+1]){
                    second++;
                }
            }
            while(first+1 < nums.size() && nums[first] == nums[first+1]){
                first++;
            }
        }
        return result;
    }
};
