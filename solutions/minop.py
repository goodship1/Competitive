class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        while 0 in nums:
            nums.remove(0)
            if nums == []:
                return 0
        return len(set(nums))
            
