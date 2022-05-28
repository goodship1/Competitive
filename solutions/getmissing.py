class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        get_max = len(nums)
        sorted(nums)
        for x in range(get_max+1):
            if x not in nums:
                return x 
