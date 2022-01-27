class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        a = set(nums1).intersection(nums2)
        b = set(nums1).intersection(nums3)
        c = set(nums2).intersection(nums3)
        return set().union(a,b,c)
