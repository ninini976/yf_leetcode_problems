class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        k = [0 for i in range(n)]
        k[0] = 1
        # use a,b,c to denote the index of 'candidate' to multiply by 2,3,5
        a = 0 
        b = 0
        c = 0
        for i in range(1,n):
            #print('i:', i)
            # pick the smallest one
            k[i] = min(k[a]*2, k[b]*3, k[c]*5)
            #print(k[i])
            if k[a]*2 == k[i]:
                a += 1
            if k[b]*3 == k[i]:
                b += 1
            if k[c]*5 == k[i]:
                c += 1
        return k[n-1]
