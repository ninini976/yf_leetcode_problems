class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(!strs.size()) return "";
        if(strs.size() == 1) return strs[0];
        string result;
        int i = 0;
        while(i<strs[0].size()){
            char c = strs[0][i];
            for(int j = 1; j < strs.size(); j++){
                if(i>strs[j].size()-1){
                    return result;    
                }
                if(strs[j][i] != c){
                    return result;                    
                }
            }
            result += c;
            i++;
        }
        return result;
    }
};
