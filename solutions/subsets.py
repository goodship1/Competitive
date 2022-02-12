from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        store = []
        for x in range(0,len(nums)+1):
            for y in combinations(nums,x):
                store.append(list(y))
        return store
