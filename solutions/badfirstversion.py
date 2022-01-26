# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start =  1
        end=n
        if start == end:
            return start
        while start < end:
            mid = (start+end)//2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid+1
        return end
                
