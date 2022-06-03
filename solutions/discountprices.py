class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        s = sentence.split()
        for x in range(len(s)):
            if s[x][0] =='$':
                try:
                    store = int(s[x][1:])
                    new_price = ''
                    new_price+=s[x][0]
                    dis = (store*discount) / 100
                    apply = store - dis
                    apply = "{:.2f}".format(apply)
                    s[x] = new_price+apply
                except:
                    continue
        return ' '.join(s)
    
                
                
