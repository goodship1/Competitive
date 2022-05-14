class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        min_index = [] 
        store = []
        for index,x in enumerate(sentence.split()):
            if x.startswith(searchWord):
                return index+1
        else:
            return -1
