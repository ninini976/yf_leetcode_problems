class Solution {
public:
    bool isPalindrome(int x) {
        // handle negative number
        if(x < 0 || (x%10 == 0 && x != 0)){
            return 0;
        }
        // get the right half and compare 
        int righthalf = 0;
        while(righthalf < x){
            righthalf = righthalf * 10 + x%10;
            x = x/10;
        }
        return (x==righthalf) || (x==righthalf/10);
    }
};
