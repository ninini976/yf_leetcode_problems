// key idea:
// compare A[mid], A[hi], A[lo] to determine mid is on left side of rotation point or right side
// then compare to target to determine target is on left side of mid or right side of mid


class Solution {
public:
  bool search(vector<int> A, int target) {
    int lo =0, hi = A.size()-1;
    if(hi == -1){
      return false;
    }
    int mid = 0;
    while(lo<hi){
          mid=(lo+hi)/2;
          if(A[mid]==target) return true;
          if(A[mid]>A[hi]){
              if(A[mid]>target && A[lo] <= target) hi = mid;
              else lo = mid + 1;
          }else if(A[mid] < A[hi]){
              if(A[mid]<target && A[hi] >= target) lo = mid + 1;
              else hi = mid;
          }else{
              hi--;
          }
          
    }
    return A[lo] == target ? true : false;
  }
};
