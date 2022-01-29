class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        duplicate_zero = '00'
        duplicate_one = '11'
        convert = str(bin(n))
        if duplicate_zero in convert or duplicate_one in convert:
            return False
        else:
            return True
        
