class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge =  nums1 + nums2
        n = len(merge)
        merge = sorted(merge)
        if n % 2 == 0:
            z = n // 2
            m = merge[z]
            e = merge[z-1]
            return (e+m)/2
        else:
            z  = n//2
            return merge[z]
