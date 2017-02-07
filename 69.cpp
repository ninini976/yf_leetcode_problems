class Solution {
public:
    int mySqrt(int x) {
        int left = 1; // set left = 1
        int right = x;
        int mid;
        while(left <= right){
            mid = left + (right - left)/2; // avoid overflow
            if(mid < x/mid){
                left = mid + 1;
            }else if(mid > x/mid){ // don't use mid*mid avoid overflow
                right = mid - 1;
                mid = right; // if no exact int is found, return a smaller int instead
            }else{
                return mid;
            }
        }
        return mid;
    }
};
