# be careful about things that are not allowed
# "00" "010" "001"
# prune early


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        for i in range(3):
            if i+1 > len(s)-3:
                break
            #print(s[:i+1])
            if int(s[:i+1]) < 256 and (len(s[:i+1])==1 or s[0] != '0'):
                for j in range(3):
                    if i+1+j+1 > len(s)-2:
                        break
                    #print('\t' + s[i+1:i+1+j+1])
                    if int(s[i+1:i+1+j+1]) < 256 and (len(s[i+1:i+1+j+1])==1 or s[i+1] != '0'):
                        for k in range(3):
                            #print('\t\t' + s[i+1+j+1:i+1+j+1+k+1])
                            if i+j+k+3 > len(s)-1:
                                break
                            #print('\t\t\t' + s[i+1+j+1:i+1+j+1+k+1]) 
                            if int(s[i+1+j+1:i+1+j+1+k+1]) < 256 and (len(s[i+1+j+1:i+1+j+1+k+1])==1 or s[i+j+2] != '0'):
                                    if len(s) - (i+1+j+1+k+1) > 3:
                                        continue
                                    elif int(s[i+1+j+1+k+1:]) < 256 and (len(s[i+1+j+1+k+1:])==1 or s[i+j+k+3] != '0'):
                                        res.append(s[:i+1] + '.' + s[i+1:i+1+j+1] + '.' + s[i+1+j+1:i+1+j+1+k+1] + '.' + s[i+1+j+1+k+1:])                
                        else:
                            continue
                    else:
                        continue
                                
            else:
                continue
        return res
