class Solution {
public:
    bool isValid(string s) {
        stack<char> left;
        for(int i = 0; i < s.size(); i++){
            char c = s[i];
            if(c == '[' or c == '{' or c == '('){
                left.push(c);
            }else{
                if(!left.empty() && ((left.top() == '[' && c == ']') || (left.top() == '(' && c == ')') || (left.top() == '{' && c == '}'))){
                    left.pop();
                }else{
                    return false;
                }
            }
        }
        if(left.size() != 0){
            return false;
        }
        return true;
    }
};
