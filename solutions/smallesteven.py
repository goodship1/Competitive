class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        muti = []
        res  = []
    
        for x in range(1,1000):
            muti.append(x)
        for y in muti:
            if y % n == 0 and y % 2 == 0:
                res.append(y)
        return min(res)
        
            
            
