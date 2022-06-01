class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for x in nums:
            counter = nums.count(x)
            if counter > 2:
                while counter>2:
                    nums.remove(x)
                    counter-=1
        return len(nums)
                    
        
