class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res=x^y
        count=0

        while res>0:
            if res & 1:
                count+=1
            res=res>>1
        
        return count
        
