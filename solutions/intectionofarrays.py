class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        flatten  = []
        for  x in nums:
            for y in x:
                flatten.append(y)
        count = Counter(flatten)
        count_items = count.items()
        result = [key for (key, value) in count_items if value == len(nums)]
        return sorted(result)
