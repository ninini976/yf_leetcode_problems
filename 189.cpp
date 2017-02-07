// corner case: lenght 0 array, length 1 array
// k >= n

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        if(nums.size() < 2) return;
        k = k%nums.size();
        reverse(nums, 0, nums.size() - k - 1);
        reverse(nums, nums.size() - k, nums.size()-1);
        reverse(nums, 0, nums.size()-1);
    }
    
    void reverse(vector<int>& nums, unsigned int left, unsigned int right){
    for(int i = 0;;i++){
        if(left + i < right - i){
            swap(nums[left+i], nums[right-i]);
        }else{
            break;
        }
    }
}
};
