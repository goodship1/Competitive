class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero  = []
        one = []
        two = []
        for x in nums:
            if x==0:
                zero.append(0)
            elif x==1:
                one.append(1)
            elif x==2:
                two.append(2)
        new_list = zero + one + two
        for x in range(len(nums)):
            nums[x] = new_list[x]
        
