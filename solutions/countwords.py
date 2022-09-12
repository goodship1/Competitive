class Solution:
    def countCharacters(self, words, chars):
        flag = False
        res = 0
        for x in words: 
            for y in x: 
                if x.count(y) <= chars.count(y): 
                    flag = True
                else:
                    flag = False
                    break
            if flag == True:
                res += len(x)
        return res
                res += len(x)
