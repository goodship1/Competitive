from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_elements = Counter(nums)
        common = count_elements.most_common()
        result = []
        count = 0
        for x in range(len(common)):
                if count == k:
                    break
                result.append(common[x][0])
                count+=1
        return result
        
