# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        res = float('inf')
        temp = False
        l,r = 0,n
        while l <= r:
            middle = (l+r) // 2
            if isBadVersion(middle):
                res = middle
                r = middle -1
            else:
                l = middle + 1
        return res