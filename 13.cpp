class Solution {
public:
    int romanToInt(string s) {
        int result = 0;
        for(int i = 0; i<s.size();i++){
            char c = s.at(i);
            switch (c){
                case 'I':
                    if(i != s.size()-1) result += s[i+1]=='X'||s[i+1]=='V'?-1:1;
                    else result += 1;
                    break;
                case 'V':
                    result += 5;
                    break;
                case 'X':
                    if(i != s.size()-1) result += s[i+1]=='L'||s[i+1]=='C'?-10:10;
                    else result += 10;
                    break;
                case 'L':
                    result += 50;
                    break;
                case 'C':
                    if(i != s.size()-1) result += s[i+1]=='D'||s[i+1]=='M'?-100:100;
                    else result += 100;
                    break;
                case 'D':
                    result += 500;
                    break;
                case 'M':
                    result += 1000;
                    break;
                default:
                    continue;
            }
        }
        return result;
    }
};
