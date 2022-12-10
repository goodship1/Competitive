class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        to_a =  [x for x in range(1,a+1)]
        to_b = [y for y in range(1,b+1)]
        store_a = []
        store_b = []
        for x in to_a:
            if a % x == 0:
                store_a.append(x)
        for y in to_b:
             if b  % y  == 0:
                store_b.append(y)
        s = set(store_a)
        b = set(store_b)
        return len(s.intersection(b))
        
        
                
                
        
        
