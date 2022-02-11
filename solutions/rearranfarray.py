class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = []
        arr_one = []
        arr_two = []
        for x in nums:
            if x >0:
                arr_one.append(x)
            else:
                arr_two.append(x)
        for x in range(len(arr_one)):
            res.append(arr_one[x])
            res.append(arr_two[x])
        return res
        
