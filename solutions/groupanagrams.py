class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = collections.defaultdict(list)
        for x in strs:
            store[''.join(sorted(x))].append(x)
        return store.values()
