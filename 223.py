
# very important corner case:
# when two rectangles do not overlap 

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        xs = sorted([A,C,E,G])
        x = abs(xs[1] - xs[2]) if not min(A,C) > max(E,G) and not max(A,C) < min(E,G) else 0
        ys = sorted([B,D,F,H]) 
        y = abs(ys[1] - ys[2]) if not min(B,D) > max(F,H) and not max(B,D) < min(F,H) else 0
        
        return abs(A-C) * abs(B-D) + abs(E-G)*abs(F-H)- x*y
