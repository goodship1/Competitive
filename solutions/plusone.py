class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        number = ''
        for x in digits:
            number+=str(x)
        number = int(number)+1
        for x in str(number):
            res.append(int(x))
        return res
        
