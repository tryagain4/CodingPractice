# implement Add without using + and -
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """                      
        def add(x,y,l):            
            if (x == 0):
                if (l == 0):
                    return y
                else:
                     return add(y,l,0)
            if (y == 0):
                if (l == 0):
                    return x
                else:
                    return add(x,l,0)
            m = 1&x
            n = 1&y
            ret = m^n^l
            l = (m&n)|(m&l)|(n&l)
            return (add(x>>1, y>>1, l) << 1)|ret
        
        def minus(x,y,l):
            print x,y,l
            if y == 0:
                if l == 0:
                    return x
                else:
                    return minus(x,l,0)
            m = 1&x
            n = 1&y
            ret = m^n^l
            if m > n: l = 0
            if m < n: l = 1            
            return minus(x>>1,y>>1,l)<<1 | ret
        
        a0 = abs(a)
        b0 = abs(b)
        
        if a >= 0:
            if b >= 0: 
                return add(a,b,0)
            else:
                return minus(a0,b0,0) if a0 >= b0 else -minus(b0,a0,0)
        else:
            if b >= 0:
                return -minus(a0,b0,0) if a0 >= b0 else minus(b0,a0,0)
            else:
                return -add(a0,b0,0)
            
        
        