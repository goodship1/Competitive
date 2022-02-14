from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        result = []
        for x in count:
            if count[x]==2:
                result.append(x)
        return result
