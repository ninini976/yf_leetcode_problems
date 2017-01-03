#include <algorithm> 
class Solution {
public:
    int maxArea(vector<int>& height) {
        int len = height.size();
        int left = 0;
        int right = len - 1;
        int maxarea = 0;
        while(left < right){
            maxarea = max(maxarea, min(height[left], height[right]) * (right - left));
            if(height[right] >= height[left]){
                left++;
            }else{
                right--;
            }
        }
        return maxarea;
    }
};
