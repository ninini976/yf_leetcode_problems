class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if(!s.size()){
            return 0;
        }
        int idx1 = 0;
        int idx2 = 1;
        unordered_map<char,int> map;
        map.insert(make_pair(s[0],0));
        int longest = 1;
        int currentlength = 1;
        while(idx2 < s.size()){
            //cout << "idx1:" << idx1 << " idx2: " << idx2 << '\n';
            //cout << "map size:" << map.size() << '\n';
            if(map.find(s[idx2]) == map.end() || map[s[idx2]] < idx1){ // idx2++ if the letter is not in hashmap or the position is before idx1
                //cout << "1\n";
                map.insert(make_pair(s[idx2],idx2));
                longest = max(longest, idx2-idx1+1);
                if(map[s[idx2]] < idx1){ // update the position if letter on position idx2 was last seen before idx1
                    map[s[idx2]] = idx2;
                }
                idx2++;
            }else{
                //cout << "2\n";
                idx1 = map[s[idx2]]+1;
                map[s[idx2]] = idx2;
                idx2++;
            }
        }
        return longest;
    }
};
