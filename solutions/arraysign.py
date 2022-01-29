class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1 
        for x in range(len(nums)):
            product = product*nums[x]
        if product >0:
            return 1
        elif product <0:
            return -1
        elif product ==0:
            return 0
