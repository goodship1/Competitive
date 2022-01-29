class Solution:
    def findComplement(self, num: int) -> int:
        convert = str(bin(num))
        convert =  convert[2:]
        new_num = ''
        for x in convert:
            if x =='1':
                new_num+='0'
            else:
                new_num+='1'
        return int(new_num,2)
