import itertools
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #first edge case when string is empty
        if s == '':
            return 0
        
        start = 0 # start of word
        end = 0
        max_length = 0
        store = set()
        while end < len(s):
            if s[end] not in store:
                store.add(s[end])
                end+=1
                max_length = max(max_length,len(store))
            else:
                store.remove(s[start])
                start+=1
        return max_length
