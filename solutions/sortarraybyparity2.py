class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        for x in  nums:
            if x%2 ==0:
                even.append(x)
            else:
                odd.append(x)
        result = []
        for x in range(len(even)):
            result.append(even[x])
            result.append(odd[x])
        return result
