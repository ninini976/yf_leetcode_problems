class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int index1 = 0;
        int index2 = numbers.size() - 1;
        vector<int> result;
        while(true){
            if(numbers[index1] + numbers[index2] > target){
                index2--;
            }
            if(numbers[index1] + numbers[index2] < target){
                index1++;
            }
            if(index1 >= index2){
                break;
            }
            if(numbers[index1] + numbers[index2] == target){
                cout << "index1=" << (index1+1) << ", index2=" << (index2+1);
                result.push_back((index1+1));
                result.push_back((index2+1));
                index1++;
                index2--;
            }
        }
        return result;
    }
};