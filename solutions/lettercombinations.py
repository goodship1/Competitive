class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = { "2":'abc',  "3":'def',\
                     "4":'ghi',  "5":'jkl',\
                     "6":'mno',  "7":'pqrs',\
                     "8":'tuv',  "9":'wxyz'}
        
        store = [""]
        for x in digits:
            store = [i+j for i in store for j in mapping[x]]
        if store ==[""]:
            store = []
        return store
