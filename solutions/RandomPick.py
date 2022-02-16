class Solution:

    def __init__(self, nums: List[int]):
        self.nums =  nums
        

    def pick(self, target: int) -> int:
        index_dic = {}
        for index, value in enumerate(self.nums):
            if value == target:
                index_dic[index] = value
        return random.choice(list(index_dic.keys()))
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
