from math import sqrt


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if int(sqrt(num)) == sqrt(num):
            return True
        return False


s = Solution()
s.isPerfectSquare(100)