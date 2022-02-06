class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        result =  None
        store =[]
        if original in nums:
            for x in range(len(nums)):
                res = original*2
                original = res
                if res not in nums:
                    return res
        return original
