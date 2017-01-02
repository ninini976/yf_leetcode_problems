class Solution {
public:
    int myAtoi(string str) {
        int sign, base, i;
        sign = 1;
        i = 0;
        base = 0;
        // handle white space
        while(str[i]==' '){
            i++;
        }
        // handle sign
        if(str[i] == '+' || str[i] == '-'){
            sign = 1 - 2*(str[i] == '-');
            i++;
        }
        while(str[i] >= '0' && str[i] <= '9'){
            // handle overflow case
            if((base > INT_MAX/10)||(base == INT_MAX/10 && str[i]-'0' > INT_MAX%10)){
                if(sign == 1) return INT_MAX;
                else return INT_MIN;
            }
            base = base*10 + (str[i] - '0');
            i++;
        }
        return base*sign;
    }
    
};
