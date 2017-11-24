class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """                     
        def add(x,y):
            return x if y == 0 else add(x^y, (x&y)<<1)
        def minus(x,y):
            return x if y == 0 else minus(x^y, ((x^y)&y)<<1)
        
        a0 = abs(a)
        b0 = abs(b)
        
        if a >= 0:
            if b >= 0: 
                return add(a,b)
            else:
                return minus(a0,b0) if a0 >= b0 else -minus(b0,a0)
        else:
            if b >= 0:
                return -minus(a0,b0) if a0 >= b0 else minus(b0,a0)
            else:
                return -add(a0,b0)