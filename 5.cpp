class Solution {
public:
    string longestPalindrome(string s) {
        if(s.size() < 1){
            return s;
        }
        int maxlength = 0;
        int extendlength;
        int start;
        int len = s.size();
        for(int i = 0; i < len; i++){
            extendlength = extendpalindrom(s,i,i); // find odd length palindromic string
            if(extendlength > maxlength){
                maxlength = extendlength;
                start = i-(maxlength-1)/2;
            }
            extendlength = extendpalindrom(s,i,i+1); // find even length palindromic string
            if(extendlength > maxlength){
                maxlength = extendlength;
                start = i-(maxlength)/2+1;
            }
        }
        return s.substr(start, maxlength);
    }
    
    int extendpalindrom(string s, int a, int b){
        //cout << "extend " << s << " start " << a << " and " << b << '\n';
        int startlength = a==b?-1:0;
        while(s[a] == s[b] && a>=0 && b <s.size()){
            a--;
            b++;
            startlength += 2;
        }
        //cout << startlength << '\n';
        return startlength;
    }
};