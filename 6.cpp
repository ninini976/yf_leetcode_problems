/*n=numRows
Δ=2n-2    1                           2n-1                         4n-3
Δ=        2                     2n-2  2n                    4n-4   4n-2
Δ=        3               2n-3        2n+1              4n-5       .
Δ=        .           .               .               .            .
Δ=        .       n+2                 .           3n               .
Δ=        n-1 n+1                     3n-3    3n-1                 5n-5
Δ=2n-2    n                           3n-2                         5n-4
*/

class Solution {
public:
    string convert(string s, int numRows) {
        if(numRows == 1 || s.size() < numRows){
            return s;
        }
        string result = "";
        for(int i = 0; i < numRows && i < s.size(); i++){
            int start = i;
            if(i == 0 || i == numRows - 1){
                while(start < s.size()){
                    result.append(s.substr(start,1));
                    start += 2*numRows-2;
                }
            }else{
                int step1 = 2*(numRows- 1 - i);
                int step2 = 2*(i);
                int step = 1;
                while(start < s.size()){
                    result.append(s.substr(start,1));
                    start += step==1 ? step1:step2;
                    step = step==1 ? 2:1;
                }
            }
        }
        return result;
    }
};